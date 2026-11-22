from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel
from schemas import Patient_details,result
from models import Patient
import pickle

with open("Diabetes_model.pkl","rb") as file:
    model=pickle.load(file)



app=FastAPI()
@app.post("/result/{Patient_id}",response_model=result,status_code=status.HTTP_200_OK)
def predict(Patient_id:int,patient:Patient_details):
    new_patient=Patient(**patient.model_dump())
    if Patient_id in Patient:
        raise HTTPException(status_code=409,detail="patient already existed")
    Patient[Patient_id]=new_patient
    input_data=[list(Patient.values())]
    prediction=model.predict(input_data)

    return {
        "Prediction":prediction
    }

@app.get("/result",response_model=list[Patient],status_code=status.HTTP_200_OK)
def patient_details():
    return list(Patient.values())

@app.get("/result/{Patient_id}",response_model=Patient,status_code=status.HTTP_200_OK)

def patient_detail(Patient_id:int):
    if Patient_id not in Patient:
        raise HTTPException(status_code=404,detail="Patient not found")
    return Patient[Patient_id]



