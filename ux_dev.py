# main.py
import json
import random
import logging
import configs.settings as settings
import tempfile
from datetime import datetime
from fastapi import FastAPI
from configs.schemas_validation import RequestData

from prompts.midjourney_prompt import mj_instructions, mj_prompt
from prompts.persona_prompt import persona_image_instructions, define_needs_prompt, generate_persona
import services.data_service as df
from services.generation_service import ImageGenerator, GPTGenerator

from prompts.profile_prompt import generate_profile_prompt
from prompts.empathy_prompt import empathy_instructions

app = FastAPI()

def initialize_managers():
    gcs_manager = df.GCSManager(settings.GCS_BUCKET)
    image_generator = ImageGenerator()
    gpt = GPTGenerator(settings.OPENAI_CLIENT)
    return gcs_manager, image_generator, gpt

def generate_profile(gpt, session_id, submission, age_min=None, age_max=None):
    profile_prompt = generate_profile_prompt(age_min=age_min, age_max=age_max)
    profile = gpt.generate_response(instructions=profile_prompt, session_id=session_id, data=submission)
    if profile.startswith("```json") and profile.endswith("```"):
        profile = profile.strip("```json").strip("```").strip()
    try:
        return json.loads(profile)
    except (json.JSONDecodeError, TypeError):
        return profile

def generate_image(gpt, image_generator, session_id, profile):
    mid_journey_prompt = gpt.generate_response(session_id=session_id, instructions=mj_instructions, data=mj_prompt(profile))
    image_data, image_id = image_generator.generate_images(mid_journey_prompt)
    return image_data

def write_to_temp_file(data_list):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as temp_file:
        json_data = json.dumps(data_list, indent=4)
        temp_file.write(json_data.encode())
        temp_file.flush()
        return temp_file.name

def upload_to_gcs(gcs_manager, destination_blob_name, file_path):
    try:
        gcs_manager.upload_to_gcs(destination_blob_name=destination_blob_name, file_path=file_path)
        logging.info(f"File uploaded to GCS at {destination_blob_name}")
    except Exception as e:
        logging.error(f"Failed to upload file to GCS: {e}")

@app.post("/process-data")
def process_data(request_data: RequestData):
    gcs_manager, image_generator, gpt = initialize_managers()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    logging.info("Storing Request Data..")
    request_data = request_data.model_dump(by_alias=True, exclude_none=True)
    session_id = request_data["session_id"]
    product_name = request_data["product_name"]

    temp_file_path = write_to_temp_file(request_data)
    upload_to_gcs(gcs_manager, f"request_data/submission_{session_id}_{timestamp}.json", temp_file_path)

    session_id = request_data["session_id"]
    num_interviews = request_data["num_interviews"]
    num_personas = request_data["num_personas"]

    age_min = request_data["default_characteristics"]["age_min"]
    age_max = request_data["default_characteristics"]["age_max"]
    
    logging.info("Starting Interviews..")
    interviews_list = []
    for _ in range(num_interviews):
        logging.info("Generating user profile..")
        profile_dict = generate_profile(gpt, session_id, request_data, age_min, age_max)
        image_data = generate_image(gpt, image_generator, session_id, profile_dict)
        uploaded_image_urls = gcs_manager.download_and_upload_images(image_data, session_id)
        image = uploaded_image_urls[random.randint(0, 3)]
        interviews_list.append({
            "session_id": session_id, 
            "product_name": product_name,
            "problem_to_solve": request_data["problem_to_solve"],
            "product_type": request_data["product_type"],
            "profile": profile_dict, 
            "profile_pictures": image
            })

    temp_file_path = write_to_temp_file(interviews_list)
    upload_to_gcs(gcs_manager, f"{settings.GCS_PREFIX}/submission_{session_id}_{timestamp}.json", temp_file_path)

    user_interviews = gcs_manager.get_latest_blob(settings.GCS_PREFIX)
    empathy_map = gpt.empathy_map_generator(instructions=empathy_instructions, session_id=session_id, data=user_interviews)

    empathy_map_dict = {"session_id": session_id, "empathy_map": empathy_map}
    temp_file_path = write_to_temp_file(empathy_map_dict)
    upload_to_gcs(gcs_manager, f"empathy_maps/submission_{session_id}_{timestamp}.md", temp_file_path)

    personas_list = []
    for _ in range(num_personas):
        logging.info("Generating personas..")
        persona_instructions = generate_persona()
        user_persona_dict = gpt.generate_response(instructions=persona_instructions, session_id=session_id, data=empathy_map)

    try:
        # Attempt to decode directly in case the response is already JSON-formatted
        user_persona_dict = json.loads(user_persona_dict)
    except (json.JSONDecodeError, TypeError):
        # If decoding fails, check if it has the expected backtick wrapper
        if isinstance(user_persona_dict, str) and user_persona_dict.startswith("```json") and user_persona_dict.endswith("```"):
            try:
                # Strip the backticks and try decoding again
                user_persona_dict = json.loads(user_persona_dict.strip("```json").strip("```").strip())
            except (json.JSONDecodeError, TypeError):
                # Default to an empty dictionary if it still fails
                user_persona_dict = {}
        else:
            # Proceed with an empty dictionary if no valid JSON format is detected
            user_persona_dict = {}
            
        personas_data = {key: value if isinstance(user_persona_dict, dict) else user_persona_dict for key, value in user_persona_dict.items()}
        persona_image_prompt = gpt.generate_response(instructions=persona_image_instructions, session_id=session_id, data=personas_data)
        image_data, image_id = image_generator.generate_images(persona_image_prompt)
        uploaded_image_urls = gcs_manager.download_and_upload_images(image_data, session_id)
        image = uploaded_image_urls[random.randint(0, 3)]
        personas_list.append({"session_id": session_id, "persona": personas_data, "profile_pictures": image})

    temp_file_path = write_to_temp_file(personas_list)
    upload_to_gcs(gcs_manager, f"personas/submission_{session_id}_{timestamp}.json", temp_file_path)

    personas = gcs_manager.get_latest_blob(path_prefix="personas/")
    user_needs = gpt.define_user_needs(instructions=define_needs_prompt, personas_data=personas, interviews_data=interviews_list, session_id=session_id)

    user_needs_dict = {"session_id": session_id, "user_needs": user_needs}
    temp_file_path = write_to_temp_file(user_needs_dict)
    upload_to_gcs(gcs_manager, f"user_needs/submission_{session_id}_{timestamp}.md", temp_file_path)

    return {"status": "success"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)