from fastapi import FastAPI,status,HTTPException,Depends
from sqlalchemy.orm import Session,selectinload
from pydantic import BaseModel
from schemas import Patient_details,result
from models import Patient
from database import get_db,Base,engine
import pickle

with open("Diabetes_model.pkl","rb") as file:
    model=pickle.load(file)

app=FastAPI()
Base.metadata.create_all(bind=engine)
@app.post("/result/{Patient_id}",response_model=Patient_details,status_code=status.HTTP_200_OK)
def predict(Patient_id:int,patient:Patient_details,db:Session=Depends(get_db)):
    new_pateint=Patient(**patient.model_dump())
    db.add(new_pateint)
    db.commit()
    db.refresh(new_pateint)
    return new_pateint
@app.get("/patients/{Patient_id}",response_model=Patient_details,status_code=status.HTTP_202_ACCEPTED)
def patient_individual_details(Patient_id:int,db:Session=Depends(get_db)):
    patient=db.get(Patient,Patient_id)
    if patient is None:
        raise HTTPException(status_code=404,detail="Patient not found")
    return patient
@app.get("/patients/",response_model=list[Patient_details],status_code=status.HTTP_202_ACCEPTED)
def patient_all_details(db:Session=Depends(get_db)):
    Patients=db.query(Patient).all()

    return Patients

@app.put("/result/{Patient_id}",response_model=Patient_details,status_code=status.HTTP_200_OK)
def update_patient_details(Patient_id:int,Patient_details:Patient_details,db:Session=Depends(get_db)):
    Patient=db.get(Patient,Patient_id)
    if Patient is None:
        raise HTTPException(status_code=404,detail="Patient not found")
    Patient.Gender=Patient_details.Gender
    
 
















































































































































