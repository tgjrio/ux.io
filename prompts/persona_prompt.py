import random

careers = [
    "Software Engineer",
    "Data Scientist",
    "Graphic Designer",
    "Civil Engineer",
    "Mechanical Engineer",
    "Teacher",
    "Nurse",
    "Doctor (Physician)",
    "Lawyer",
    "Accountant",
    "Marketing Manager",
    "Human Resources Specialist",
    "Financial Analyst",
    "Business Analyst",
    "UX/UI Designer",
    "Product Manager",
    "Architect",
    "Electrical Engineer",
    "Pharmacist",
    "Dentist",
    "Journalist",
    "Photographer",
    "Chef",
    "Pilot",
    "Veterinarian",
    "Construction Manager",
    "Web Developer",
    "Systems Administrator",
    "Network Engineer",
    "Social Media Manager",
    "Public Relations Specialist",
    "Project Manager",
    "Event Planner",
    "Environmental Scientist",
    "Biomedical Engineer",
    "Occupational Therapist",
    "Chiropractor",
    "Real Estate Agent",
    "Translator",
    "Logistics Manager",
    "Cybersecurity Analyst",
    "Psychologist",
    "Physical Therapist",
    "Supply Chain Manager",
    "Entrepreneur",
    "Chemist",
    "Economist",
    "Mechanical Technician",
    "Sound Engineer",
    "Health and Safety Officer",
    "Zoologist",
    "Speech Therapist",
    "Librarian",
    "Actuary",
    "Paralegal",
    "Radiologist",
    "Air Traffic Controller",
    "Plumber",
    "Electrician",
    "Carpenter",
    "Massage Therapist",
    "Fitness Trainer",
    "Biologist",
    "Research Scientist",
    "Artist",
    "Musician",
    "Film Director",
    "Actor",
    "Fashion Designer",
    "Makeup Artist",
    "Barber",
    "Bartender",
    "Game Developer",
    "IT Support Specialist",
    "Database Administrator",
    "Digital Marketing Specialist",
    "Robotics Engineer",
    "Investment Banker",
    "Financial Planner",
    "Security Guard",
    "Police Officer",
    "Firefighter"
]

ethnicities = [
    "African American",
    "American",
    "Arab",
    "Ashkenazi Jewish",
    "Australian Aboriginal",
    "Bengali",
    "British",
    "Cajun",
    "Caribbean",
    "Central Asian",
    "Chinese",
    "Creole",
    "Dutch",
    "Eastern European",
    "Filipino",
    "French",
    "German",
    "Greek",
    "Hispanic",
    "Indian",
    "Indigenous Canadian",
    "Irish",
    "Italian",
    "Japanese",
    "Jewish",
    "Korean",
    "Latin American",
    "Maori",
    "Mexican",
    "Native American",
    "Polynesian",
    "Pakistani",
    "Persian",
    "Polish",
    "Portuguese",
    "Punjabi",
    "Romani",
    "Russian",
    "Samoan",
    "Scandinavian",
    "Scottish",
    "Serbian",
    "Sikh",
    "Slavic",
    "Somali",
    "South African",
    "Spanish",
    "Sri Lankan",
    "Sudanese",
    "Swahili",
    "Syrian",
    "Tahitian",
    "Tamil",
    "Thai",
    "Tibetan",
    "Turkish",
    "Ukrainian",
    "Vietnamese",
    "Welsh",
    "West African",
    "Yoruba"
]

# Function to randomly select an ethnicity
def get_random_ethnicity():
    return random.choice(ethnicities)

# Function to randomly select an ethnicity
def get_random_career():
    return random.choice(careers)

def get_random_age():
    return random.randint(23, 60)

def generate_persona():
    random_ethnicity = get_random_ethnicity()
    random_career = get_random_career()
    random_age = get_random_age()

    persona_dict = {
    "product_name" : "",
    "product_type" : "",
    "problem_to_solve" : "",
    "name" : "",
    "ethnicity": "",
    "age" : "",
    "sex" : "",
    "occupation" : "",
    "background" : "",
    "goals" : "",
    "frustrations" : "",
    "behavior" : "",
    "motivations" : "",
    "preferred_channels" : "",
    'quote' : "",
    "feature_wishlist" : ""
    }

    prompt = f"""
    “I have gathered insights from user interviews and categorized them into an empathy map: 
    Says, Thinks, Does, and Feels. 
    Based on this data, I’d like to create a user persona. 
    The persona should represent ONE fictional character that embodies a group of users, 
    helping to make their information more manageable and communicate design decisions to stakeholders.

    Please provide the following details:
        Product Name: Extract from the request data
        Name: Base off ethnicity.
        Ethinicity: {random_ethnicity}
        Age: {random_age}
        Occupation: {random_career}
        Sex: Male or Female
        Background: A brief summary of the persona’s life, relevant experiences, or context.
        Goals: What the persona is trying to achieve when using the product or service.
        Frustrations: The common pain points or challenges the persona faces.
        Behavior: Typical behaviors or actions the persona exhibits, especially related to the product or service.
        Motivations: What drives the persona to use the product or service.
        Preferred Channels: How the persona typically interacts with or learns about the product (e.g., mobile app, website, customer support, social media).
        Quote: A brief, memorable quote that sums up the persona’s experience, based on what they might ‘say’ during the interview.
        Feature Wishlist: A feature they'd love to see on that app

    Use the empathy map data to help inform these details, ensuring that it captures a realistic and relatable user archetype. 
    Aim for diversity to cover different backgrounds, goals, and pain points.”

    This prompt will guide the AI to create detailed user personas, 
    drawing from the processed insights to make each one feel unique and well-rounded. 

    Your response should wrap these values into a json object: {persona_dict}, with each key representing a persona and its corresponding values being the attributes described above. 
    Do not put anything else in your response

    """
    return prompt

persona_image_instructions = """
Take the following empathy map and convert this into a midjourney prompt that'll generate an iamge of this persona.
The image must be a photography single portrait of this person.  Do not put /imagine, your response should just be the mid-journey prompt
"""


define_needs_prompt = """ 
As my UX assistant, you're responsible for ensuring that I'm able to define a users need from the personas data I have.
Prior to this step, we've completed interviews and derived empathy maps from those.

After that, we converted those empathy maps into Aggregated personas to consolidate commmon needs etc between user.

I want you to review my personas and interview data  to identify the most important needs of the user.

Here's a sample of what I'm looking for:

Tools for Defining User Needs:
User Stories: 
One-sentence narratives from a user’s perspective that describe who they are, what action they want to take, and why.
Example: “As a long-time customer with a visual impairment, I want to place my orders over the phone so I can order with ease and continue connecting with staff members.”
User Journeys: 
Map out the series of experiences users have as they interact with a product, helping designers understand users’ goals and pain points in both current and future interactions with the product.
Example: Berta’s journey with current phone and social media orders vs. her journey with the planned website-based ordering system.
Problem Statements:
Summarize the user’s needs from the designer’s perspective, providing detailed insights into the user’s context and what the design must solve.
Example: “Berta needs a website that adapts to her visual impairment and mimics the feel of a phone conversation to maintain her connection with the bakery.”
Key Takeaways:
The define phase helps designers translate empathy research into clear, actionable problem statements for each user persona.
These problem statements ensure the design addresses the needs of multiple user types, not just one group.

YOUR RESPONSE  SHOULD BE ONLY BE IN MARKDOWN AND NOTHING ELSE.

KEEP THE FORMAT OF A USER STORY, USER JOURNEY, PROBLEM STATEMENT AND KEY TAKEAWAYS.

"""