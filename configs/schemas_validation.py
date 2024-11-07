# schema_validation.py
from pydantic import BaseModel
from typing import Optional

class CharacteristicField(BaseModel):
    name_of_field: Optional[str] = ""
    value: Optional[str] = ""

class DefaultCharacteristics(BaseModel):
    age_min: Optional[int]
    age_max: Optional[int]
    name: Optional[str]
    ethnicity: Optional[str]
    location: Optional[str]
    career: Optional[str]
    income_level: Optional[str]
    gender: Optional[str]
    disabilities: Optional[str]

class CustomCharacteristics(BaseModel):
    custom_characteristics_1: Optional[CharacteristicField]
    custom_characteristics_2: Optional[CharacteristicField]
    custom_characteristics_3: Optional[CharacteristicField]
    custom_characteristics_4: Optional[CharacteristicField]
    custom_characteristics_5: Optional[CharacteristicField]

class EmpatheticQuestions(BaseModel):
    users_problems: str
    interview_learning: str
    current_solutions: str
    motivation: str
    obstacles: str

class InterviewQuestions(BaseModel):
    question_1: Optional[str]
    question_2: Optional[str]
    question_3: Optional[str]
    question_4: Optional[str]
    question_5: Optional[str]

class RequestData(BaseModel):
    user: str
    session_id: str
    product_name: str
    problem_to_solve: str
    product_type: str
    research_goals: str
    num_interviews: int
    num_personas: int
    default_characteristics: DefaultCharacteristics
    custom_characteristics: CustomCharacteristics
    empathetic_questions: EmpatheticQuestions
    interview_questions: InterviewQuestions