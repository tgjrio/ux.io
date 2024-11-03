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

def get_random_age(age_min:int = None, age_max:int = None):
    if age_min and age_max:
        return random.randint(age_min, age_max)
    else:
        return random.randint(23, 60)


sample_dict = {
    'age': '', 
	'name': '', 
	'ethnicity': '', 
	'location': '', 
	'career': '', 
	'income_level': '', 
	'gender': '', 
	'disabilities': '',
    "custom_characteristics" : {
        "custom_characteristics_1": {"name_of_field": "", "value": ""},
        "custom_characteristics_2": {"name_of_field": "", "value": ""},
        "custom_characteristics_3": {"name_of_field": "", "value": ""},
        "custom_characteristics_4": {"name_of_field": "", "value": ""},
        "custom_characteristics_5": {"name_of_field": "", "value": ""}
    },
	"empathetic_questions" : {},
    "interview_questsions": {}
}

# Function to generate the rules string with a random ethnicity
def generate_profile_prompt(age_min, age_max):
    random_ethnicity = get_random_ethnicity()
    random_career = get_random_career()
    random_age = get_random_age(age_min, age_max)

    instructions = f"""
    YOUR JOB AS MY ASSISTANT IS TO CREATE USER PROFILES FOR UX DESIGNERS TO WORK WITH.  INSTEAD OF DOING THE TRADITIONAL IN PERSON INTERVIEW, 
    YOU WILL CURATE PROFILES BASED ON THE DATA YOU'RE GIVEN.

    I NEED YOU TO RETURN A JSON OBJECT THAT WILL REPRESENT THE PROFILE OF THIS PERSON.  
    YOU WILL LOOK IN THE participant_characteristics OBJECT AND RECREATE THE
    JSON WHILE FOLLOWING STRUCTURE BELOW:

    {sample_dict}

    IN ORDER TO GENERATE THESE VALUES:
        
        For Career: {random_career}
        For Ethnicity: {random_ethnicity}
        For Location, make sure it's in the United States and format is City, State
        For Income Level, make sure it aligns with the career. Format response like: $xxk-$xxk
        For Age: {random_age}
        For Gender, it should be either Male or Female
        For Disabilities, Random
        For Name, should align with Ethnicity
        For Custom Characteristics Characteristics Fields, generate a value by using the name of the field and character profile
        For Empathetic Questions, generate answers to the questions based on the user's profile and it should read as if they typed it themselves
        For Interview Questions, generate answers to the questions based on the user's profile and it should read as if they typed it themselves


       **VERY IMPORTANT THAT ALL FIELDS ARE FILLED IN AND THAT THE JSON FIELDS ARE IN THE SAME ORDER AS THIS SAMPLE {sample_dict}**
        
    YOUR RESPONSE SHOULD ONLY BE A STRING JSON AND NOTHING ELSE
    """
    return instructions