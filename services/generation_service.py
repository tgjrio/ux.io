from datetime import datetime
import time
import requests
import json
import tempfile
import configs.settings as settings
import logging
import services.data_service as df
from typing import Any, Dict, Optional, Tuple


class GPTGenerator:
    def __init__(self, client: Any):
        self.client = client
        self.gcs_manager = df.GCSManager(settings.GCS_BUCKET)

    def format_response_to_dict(self, instructions: str, response: Any, session_id: str, data: str) -> None:
        try:
            performance_data = {
                "session_id": session_id,
                "id": response.id,
                "created_at": response.created,
                "completion_tokens": response.usage.completion_tokens,
                "prompt_tokens": response.usage.prompt_tokens,
                "total_tokens": response.usage.total_tokens
            }
            message_data = {
                "session_id": session_id,
                "instructions": instructions,
                "content": data,
                "message": response.choices[0].message.content if response.choices else None
            }

            logging.info(f"Performance Data: {performance_data}")

            self.upload_analytics_data(performance_data, session_id)
            self.upload_message_data(message_data, session_id)

            logging.info("Data loaded successfully!")
        except Exception as e:
            logging.error(f"Failed to format response to dict: {e}")

    def upload_analytics_data(self, performance_data: Dict[str, Any], session_id: str) -> None:
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as temp_file:
                json_data = json.dumps(performance_data, indent=4)
                temp_file.write(json_data.encode())
                temp_file.flush()
                temp_file_path = temp_file.name
                
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            destination_blob_name = f"performance_data/session_{session_id}_{timestamp}.json"
            self.gcs_manager.upload_to_gcs(destination_blob_name, temp_file_path)
        except Exception as e:
            logging.error(f"Failed to write analytics data to temp file or upload to GCS: {e}")

    def upload_message_data(self, message_data: Dict[str, Any], session_id: str) -> None:
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as temp_file:
                json_data = json.dumps(message_data, indent=4)
                temp_file.write(json_data.encode())
                temp_file.flush()
                temp_file_path = temp_file.name

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            destination_blob_name = f"message_data/session_{session_id}_{timestamp}.json"
            self.gcs_manager.upload_to_gcs(destination_blob_name, temp_file_path)
        except Exception as e:
            logging.error(f"Failed to write message data to temp file or upload to GCS: {e}")

    def generate_response(self, session_id: str, instructions: str, data: str, task_type: str = "generic") -> str:
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",
                max_tokens=16384,
                messages=[
                    {"role": "system", "content": instructions},
                    {"role": "user", "content": f"Here's the data: {data}"},
                ]
            )

            result = response.choices[0].message.content
            self.format_response_to_dict(instructions=instructions, response=response, session_id=session_id, data=result)

            return result
        except Exception as e:
            logging.error(f"Failed to generate response: {e}")
            return ""

    def empathy_map_generator(self, instructions: str, data: str, session_id: str, file_path: str = "empathy_map.json") -> str:
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",
                max_tokens=16384,
                messages=[
                    {"role": "system", "content": instructions},
                    {"role": "user", "content": f"Here's the data: {data}"},
                ]
            )

            empathy_md = response.choices[0].message.content
            self.format_response_to_dict(instructions=instructions, response=response, session_id=session_id, data=empathy_md)

            self.save_to_file(empathy_md, file_path, "Empathy map")

            return empathy_md
        except Exception as e:
            logging.error(f"Failed to generate empathy map: {e}")
            return ""

    def define_user_needs(self, instructions: str, personas_data: str, interviews_data: str, session_id: str, file_path: str = "user_needs.md") -> str:
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",
                max_tokens=16384,
                messages=[
                    {"role": "system", "content": instructions},
                    {"role": "user", "content": f"Here's the personas: {personas_data}"},
                    {"role": "user", "content": f"Here's the interviews: {interviews_data}"},
                ]
            )

            needs_defined = response.choices[0].message.content
            self.format_response_to_dict(instructions=instructions, response=response, session_id=session_id, data=needs_defined)

            self.save_to_file(needs_defined, file_path, "User needs")

            return needs_defined
        except Exception as e:
            logging.error(f"Failed to define user needs: {e}")
            return ""

    def save_to_file(self, content: str, file_path: str, description: str) -> None:
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(content)
            logging.info(f"{description} saved to {file_path}")
        except Exception as e:
            logging.error(f"Failed to save {description.lower()}: {e}")


class ImageGenerator:
    def __init__(self):
        self.headers = {
            'Authorization': 'Bearer 43FynxHeNrHszGCqdAix1xjelYokl5Xu',
            'Content-Type': 'application/json'
        }

    def generate_images(self, prompt: str) -> Tuple[Dict[str, Any], str]:
        try:
            data = {"prompt": prompt}
            response = self.send_request("POST", "https://cl.imagineapi.dev/items/images/", data)
            image_id = self.extract_image_id(response)

            while True:
                image_data = self.check_image_status(image_id)
                if image_data is not None:
                    return image_data, image_id
                time.sleep(5)
        except Exception as e:
            logging.error(f"Unexpected error while generating images: {e}")
            raise RuntimeError(f"Unexpected error while generating images: {e}")

    def check_image_status(self, image_id: str) -> Optional[Dict[str, Any]]:
        try:
            response = self.send_request("GET", f"https://cl.imagineapi.dev/items/images/{image_id}")
            status = response['data'].get('status', None)

            if status in ['completed', 'failed']:
                if status == 'failed':
                    error_message = response['data'].get('error_message', 'Unknown error')
                    logging.error(f"Image generation failed. Error: {error_message}")
                    raise RuntimeError(f"Image generation failed. Error: {error_message}")
                logging.info("Image generation completed.")
                return response['data']
            else:
                logging.info(f"Images are not finished generating. Status: {status}")
                return None
        except Exception as e:
            logging.error(f"Unexpected error while checking image status: {e}")
            raise RuntimeError(f"Unexpected error while checking image status: {e}")

    def send_request(self, method: str, url: str, body: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        response = requests.request(method, url, json=body, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def extract_image_id(self, response: Dict[str, Any]) -> str:
        try:
            response_data = response['data']
            if 'id' not in response_data:
                logging.error("Error: Unexpected response format.", response_data)
                raise RuntimeError("Unexpected response format while generating images.")
            return response_data['id']
        except KeyError as e:
            logging.error(f"Key error while parsing response: {e}")
            logging.error("Response Data:", response)
            raise RuntimeError(f"Key error while parsing response: {e}")