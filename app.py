from fastapi import FastAPI,status
from pydantic import BaseModel
from schemas import patient,result

app=FastAPI()
@app.post("/result",response_model=result,status_code=status.HTTP_200_OK)
def predict(patient:patient):
    print(patient.age)
    prediction=2
    return {
        "Prediction":prediction
    }

@app.get("/result",response_model=patient,status_code=status.HTTP_200_OK)
def patient_details(patient:patient):
    return {
        "gender":gender,
        "age":age,
        "hypertension":hypertension,
        "smoking_history":smoking_history,
        "bmi":bmi,
        "HbA1c_level":HbA1c_level,
        "blood_glucose_level":blood_glucose_level
    }

