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


sample_dict = {
    'age': '', 
	'name': '', 
	'ethnicity': '', 
	'location': '', 
	'career': '', 
	'income_level': '', 
	'gender': '', 
	'disabilities': '', 
	"empathetic_questions" : {},
    "additional_fields" : {},
    "interview_questsions": {}
}

# Function to generate the rules string with a random ethnicity
def generate_rules():
    random_ethnicity = get_random_ethnicity()
    random_career = get_random_career()
    random_age = get_random_age()
    rules_1 = f"""
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
        For Income Level, make sure it aligns with the career. Format response like: $50k-$75k
        For Age: {random_age}
        For Gender, it should be either Male or Female
        For Disabilities, Random
        For Name, should align with Ethnicity
        For Empathetic Questions, generate answers to the questions based on the user's profile and it should read as if they typed it themselves
        For Additional Fields, they will come with instructions

        Next, you'll create a key:value pair of the following questions.  Please answer these as if you have this users profile:

        question_1: Can you walk me through your current process of finding and using recipes to plan meals?
        question_2: How do you currently create your grocery list when using a recipe? What steps do you follow, and what challenges do you encounter?
        question_3: Have you ever missed or forgotten ingredients when following a recipe? What do you think contributed to that?
        question_4: What tools or methods do you currently use to organize your meal planning and grocery shopping? How do they work for you?
        question_5: Can you describe a time when creating a grocery list felt particularly frustrating or time-consuming? How did you handle it?
        question_6: How do you decide what meals to cook during a typical week? What role do recipes play in that process?
        question_7: When looking at a new recipe, what factors do you consider before deciding to add it to your meal plan?
        question_8: How do you usually deal with recipes that have a long list of ingredients? How does that impact your meal planning or grocery shopping?
        question_9: Have you ever found it difficult to keep track of all the ingredients you need across multiple recipes? How do you manage that?
        question_10: What would an ideal solution for managing your grocery lists from recipes look like to you?

       **VERY IMPORTANT THAT ALL FIELDS ARE FILLED IN AND THAT THE JSON FIELDS ARE IN THE SAME ORDER AS THIS SAMPLE {sample_dict}**
        
    YOUR RESPONSE SHOULD ONLY BE A STRING JSON AND NOTHING ELSE
    """
    return rules_1

def generate_persona():
    random_ethnicity = get_random_ethnicity()
    random_career = get_random_career()
    random_age = get_random_age()

    persona_dict = {
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


empathy_instructions = """
As my UX assistant, you are responsible for creating an Aggregated Empathy map from all the interviews I conducted. 
Below is your list of instructions:


Fill in the “Says” Section: Record direct quotes from the interview.
Fill in the “Thinks” Section: Summarize the user’s thoughts, including any inferred feelings.
Fill in the “Does” Section: Document the actions the user takes based on their challenges.
Fill in the “Feels” Section: Record emotions expressed or inferred during the interview.

1. Extract and Process Interview Data:
	•	Analyze the provided interview data to extract relevant information:
	•	Review the raw interview data (transcripts, notes, or responses) to understand the overall context.
	•	Ensure data is cleaned (removing irrelevant content, filler words, and noise) for accurate analysis.
	•	Identify key phrases, sentences, or patterns that provide insights into user behavior, thoughts, and emotions:
	•	Keyword Extraction:
	•	Highlight keywords related to the product, service, or experience being analyzed.
	•	Focus on repeated words or phrases that indicate common themes or issues.
	•	Thematic Analysis:
	•	Group keywords into broader themes (e.g., “usability,” “frustration,” “features”) to understand larger patterns.
	•	Use tags or labels for common responses to help organize findings.
	•	Sentiment Analysis:
	•	Determine the sentiment behind statements (positive, negative, neutral) to gauge user attitudes.
	•	Identify specific emotions (e.g., happiness, frustration, confusion) based on tone and context.
	•	Behavioral Cues:
	•	Look for descriptions of actions users take, such as steps in a process or habitual behaviors.
	•	Note any sequences or patterns in user behavior to identify workflows and pain points.
	•	Quotes and Direct Feedback:
	•	Extract direct quotes that can be used to support findings or illustrate user experiences.
	•	Identify standout comments that are particularly insightful or impactful.
	•	Contextual Understanding:
	•	Identify the ‘Why’ Behind Statements:
	•	Consider why users express certain feelings or take specific actions.
	•	Use follow-up questions or inferred context to clarify the reasoning behind their behaviors.
	•	Correlate Behaviors with Emotional Responses:
	•	Connect actions described by users with the emotions they express (e.g., “I struggle with finding the checkout button” could indicate confusion or frustration).
	•	Cross-Reference with Previous Data:
	•	Compare current findings with any historical or past interview data to identify trends over time.
	•	Identify Gaps or Missing Information:
	•	Note areas where additional data might be needed, such as unclear responses or unaddressed questions.
	•	Consider generating follow-up questions to fill these gaps in future interviews.

By following these steps, you can effectively extract, process, and organize interview data to generate valuable insights into user experiences, helping build more accurate empathy maps.

2. Step 2: Mapping to Quadrants

	•	Create logic to categorize extracted information into four quadrants:
	•	The goal is to break down the user insights into distinct categories to better understand their experiences, thoughts, actions, and emotions.

Says:
    •   Add the User’s Name: Include the name of the person interviewed.
	•	Identify and extract direct quotes from the interview responses:
	•	Look for verbatim statements that capture what users explicitly say about their experiences.
	•	Highlight any phrases that clearly express user opinions, preferences, or feedback.
	•	Focus on phrases that indicate clear opinions, preferences, or specific feedback:
	•	Examples include statements that show approval, disapproval, suggestions, or specific issues (e.g., “I love using this product because…”).
	•	Prioritize quotes that are particularly detailed or descriptive, as they often provide deeper insights.
	•	Use Contextual Cues to Enhance Understanding:
	•	Consider the context around each quote to better understand the user’s intent and tone.
	•	If the user is giving praise or criticism, identify which aspect of the product or experience they are referring to.

Thinks:

	•	Use Natural Language Processing (NLP) to infer statements that reflect the user’s internal thoughts:
	•	Analyze the data for implied or indirect statements that reveal what users might be thinking.
	•	Derive insights from responses where users imply desires, concerns, or uncertainties, even if they are not stated outright.
	•	Identify phrases that suggest opinions, doubts, or internal decision-making:
	•	Look for phrases like “I wish…”, “I think…”, “I’m not sure if…”, “I’d prefer if…”, etc., to uncover underlying thoughts.
	•	Consider using sentiment analysis and language models to detect and categorize these inferred thoughts more accurately.
	•	Incorporate Context to Interpret Thoughts:
	•	Contextualize thoughts with specific scenarios to understand why users feel the way they do.
	•	If users are indecisive or express doubts, correlate these with specific features or experiences they interacted with.

Does:

	•	Extract action verbs and observable behavior patterns from the interview data:
	•	Identify verbs and actions that describe what users physically do when interacting with a product (e.g., “searches,” “navigates,” “clicks”).
	•	Look for recurring actions that indicate routine behavior, such as “I always…” or “I never…”.
	•	Identify phrases indicating what the user does, actions they take, or behaviors they exhibit:
	•	Categorize behaviors that reflect specific tasks users undertake, such as “I search for reviews before buying” or “I use the app mainly to…”.
	•	Recognize any step-by-step descriptions, as these can reveal pain points or areas for improvement in the user journey.
	•	Highlight Key Actions for Behavior Mapping:
	•	Prioritize actions that align with core use cases, workflows, or user journeys.
	•	Identify friction points where users struggle or express frustration with certain tasks.

Feels:

	•	Use sentiment analysis or keyword matching to identify statements that express the user’s emotions:
	•	Automatically detect the tone and sentiment of the user’s responses to determine their emotional state (e.g., happy, confused, frustrated).
	•	Match keywords that indicate emotions (e.g., “excited,” “annoyed,” “worried”) to classify feelings accurately.
	•	Recognize and categorize feelings based on positive, negative, or neutral sentiments, or pre-defined emotion keywords:
	•	Group emotions into categories to help identify overall sentiment trends across different users.
	•	Example keywords:
	•	Positive: “satisfied,” “happy,” “relieved.”
	•	Negative: “frustrated,” “annoyed,” “disappointed.”
	•	Neutral: “okay,” “fine,” “indifferent.”
	•	Understand Emotional Triggers:
	•	Pinpoint the features or experiences that elicit strong emotions, whether positive or negative.
	•	Analyze how emotional responses align with actions or thoughts to gain a deeper understanding of the user’s overall experience.

Summary:

	•	By categorizing user data into these four quadrants, you can build a comprehensive empathy map that reveals:
	•	What users explicitly say and how they communicate their needs and feedback.
	•	What users think, including their concerns, desires, and thought processes.
	•	What actions users take, highlighting their behaviors and routines.
	•	What users feel, providing insights into their emotional experiences and triggers.
	•	Use these insights to inform design decisions, identify pain points, and create more user-centered solutions.

3.	Step 3: Generate the Empathy Map
•	Combine all processed data into a structured empathy map:
•	Organize the information into the 5 quadrants: Says, Thinks, Does, Feels and Summary.
•	Ensure that each quadrant captures concise, clear information reflecting the user’s experience.
•	Output the empathy map as a markdown
•	Include clear headers and categorize content under each quadrant for easy readability.

4.	Additional Considerations:
•	Ensure extracted quotes and phrases retain their original meaning and context. 
•	For better insights, include an option to flag or highlight recurring themes or keywords across different interview responses.

PLEASE MAKE SURE YOUR RESPONSE IS JUST THE MARKDOWN  CODE FOR THE EMPATHY MAP.
PLEASE BE VERY THOROUGH IN THE AMOUNT OF CONTEXT YOU RETURN. IT DOESN'T NEED TO BE ALL BULLETS, I NEED AS MUCH DETAIL AS POSSIBLE.
DO NOT USE THE NAMES OF THE INTERVIEWEES IN THE RESPONSE. 

"""