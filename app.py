from fastapi import FastAPI
from pydantic import BaseModel


def patient(BaseModel):
    gender:str
    age:float
    hypertension:int
    smoking_history:str
    bmi:float
    HbA1c_level:float
    blood_glucose_level:int

def result(BaseModel):
    Prediction:int


app=FastAPI()
@app.post("/result/{gender,age,hypertension,smoking_history,bmi,HbA1c_level,blood_glucose_level}",response_model=result)
def predict(gender:str,age:float,hypertension:int,smoking_history:str,bmi:float,HbA1c_level:float,blood_glucose_level:int):
    return {2}
