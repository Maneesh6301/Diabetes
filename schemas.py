from pydantic import BaseModel,ConfigDict


class Patient_details(BaseModel):
    gender:str
    age:float
    hypertension:int
    smoking_history:str
    bmi:float
    HbA1c_level:float
    blood_glucose_level:int

class result(BaseModel):
    Prediction:int
    model_config=ConfigDict(from_attributes=True)