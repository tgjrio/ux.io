from google.cloud import bigquery

empathy_maps_schema = [
    bigquery.SchemaField("session_id", "STRING"),
    bigquery.SchemaField("empathy_map", "STRING"),
]

user_needs_schema = [
    bigquery.SchemaField("session_id", "STRING"),
    bigquery.SchemaField("user_needs", "STRING"),
]

personas_schema = [
    bigquery.SchemaField("session_id", "STRING"),
    bigquery.SchemaField("persona", "RECORD", mode="REPEATED", fields=[
        bigquery.SchemaField("name", "STRING"),
        bigquery.SchemaField("ethnicity", "STRING"),
        bigquery.SchemaField("age", "STRING"),
        bigquery.SchemaField("sex", "STRING"),
        bigquery.SchemaField("occupation", "STRING"),
        bigquery.SchemaField("background", "STRING"),
        bigquery.SchemaField("goals", "STRING"),
        bigquery.SchemaField("frustrations", "STRING"),
        bigquery.SchemaField("behavior", "STRING"),
        bigquery.SchemaField("motivations", "STRING"),
        bigquery.SchemaField("preferred_channels", "STRING"),
        bigquery.SchemaField("quote", "STRING"),
        bigquery.SchemaField("feature_wishlist", "STRING"),
    ]),
    bigquery.SchemaField("profile_pictures", "STRING"),
]

performance_data_schema = [
    bigquery.SchemaField("session_id", "STRING"),
    bigquery.SchemaField("id", "STRING"),
    bigquery.SchemaField("created_at", "TIMESTAMP"),
    bigquery.SchemaField("completion_tokens", "INTEGER"),
    bigquery.SchemaField("prompt_tokens", "INTEGER"),
    bigquery.SchemaField("total_tokens", "INTEGER"),
]

message_data_schema = [
    bigquery.SchemaField("session_id", "STRING"),
    bigquery.SchemaField("instructions", "STRING"),
    bigquery.SchemaField("content", "STRING"),
    bigquery.SchemaField("message", "STRING"),
]

request_data_schema = [
    bigquery.SchemaField("user", "STRING"),
    bigquery.SchemaField("session_id", "STRING"),
    bigquery.SchemaField("product_name", "STRING"),
    bigquery.SchemaField("problem_to_solve", "STRING"),
    bigquery.SchemaField("product_type", "STRING"),
    bigquery.SchemaField("research_goals", "STRING"),
    bigquery.SchemaField("num_interviews", "INTEGER"),
    bigquery.SchemaField("num_personas", "INTEGER"),
    
    # default_characteristics object
    bigquery.SchemaField("default_characteristics", "RECORD", mode="NULLABLE", fields=[
        bigquery.SchemaField("age_min", "INTEGER"),
        bigquery.SchemaField("age_max", "INTEGER"),
        bigquery.SchemaField("name", "STRING"),
        bigquery.SchemaField("ethnicity", "STRING"),
        bigquery.SchemaField("location", "STRING"),
        bigquery.SchemaField("career", "STRING"),
        bigquery.SchemaField("income_level", "STRING"),  # Updated from 'income' to 'income_level'
        bigquery.SchemaField("gender", "STRING"),
        bigquery.SchemaField("disabilities", "STRING"),
    ]),
    
    # custom_characteristics as an array of records for flexibility
    bigquery.SchemaField("custom_characteristics", "RECORD", mode="REPEATED", fields=[
        bigquery.SchemaField("name_of_field", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("value", "STRING", mode="NULLABLE")
    ]),

    # empathetic_questions object
    bigquery.SchemaField("empathetic_questions", "RECORD", mode="NULLABLE", fields=[
        bigquery.SchemaField("users_problems", "STRING"),
        bigquery.SchemaField("interview_learning", "STRING"),
        bigquery.SchemaField("current_solutions", "STRING"),
        bigquery.SchemaField("motivation", "STRING"),
        bigquery.SchemaField("obstacles", "STRING"),
    ]),
    
    # interview_questions object
    bigquery.SchemaField("interview_questions", "RECORD", mode="NULLABLE", fields=[
        bigquery.SchemaField("question_1", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("question_2", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("question_3", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("question_4", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("question_5", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("question_6", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("question_7", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("question_8", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("question_9", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("question_10", "STRING", mode="NULLABLE"),
    ]),
]

personas_schema = [
    bigquery.SchemaField("session_id", "STRING"),
    bigquery.SchemaField("name", "STRING"),
    bigquery.SchemaField("ethnicity", "STRING"),
    bigquery.SchemaField("age", "STRING"),
    bigquery.SchemaField("sex", "STRING"),
    bigquery.SchemaField("occupation", "STRING"),
    bigquery.SchemaField("background", "STRING"),
    bigquery.SchemaField("goals", "STRING"),
    bigquery.SchemaField("frustrations", "STRING"),
    bigquery.SchemaField("behavior", "STRING"),
    bigquery.SchemaField("motivations", "STRING"),
    bigquery.SchemaField("preferred_channels", "STRING"),
    bigquery.SchemaField("quote", "STRING"),
    bigquery.SchemaField("feature_wishlist", "STRING"),
    bigquery.SchemaField("profile_pictures", "STRING"),
]

interviews_schema = [  
    bigquery.SchemaField("session_id", "STRING"),
    bigquery.SchemaField("product_name", "STRING"),
    bigquery.SchemaField("age", "INTEGER", mode="NULLABLE"),
    bigquery.SchemaField("name", "STRING"),
    bigquery.SchemaField("ethnicity", "STRING"),
    bigquery.SchemaField("location", "STRING"),
    bigquery.SchemaField("career", "STRING"),
    bigquery.SchemaField("income", "STRING"),
    bigquery.SchemaField("gender", "STRING"),
    bigquery.SchemaField("disabilities", "STRING"),
    
   # Custom characteristics as a nested field
    bigquery.SchemaField("custom_characteristics", "RECORD", mode="REPEATED", fields=[
        bigquery.SchemaField("name_of_field", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("value", "STRING", mode="NULLABLE"),
    ]),

    # Empathetic questions fields
    bigquery.SchemaField("users_problems", "STRING"),
    bigquery.SchemaField("interview_learning", "STRING"),
    bigquery.SchemaField("current_solutions", "STRING"),
    bigquery.SchemaField("motivation", "STRING"),
    bigquery.SchemaField("obstacles", "STRING"),
    
    # Interview questions fields, nullable
    bigquery.SchemaField("question_1", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("question_2", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("question_3", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("question_4", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("question_5", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("question_6", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("question_7", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("question_8", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("question_9", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("question_10", "STRING", mode="NULLABLE"),
    
    # Profile pictures
    bigquery.SchemaField("profile_pictures", "STRING"),
]