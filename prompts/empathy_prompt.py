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