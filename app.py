from fastapi import FastAPI,status,HTTPException,Depends
from sqlalchemy.orm import Session,selectinload
from pydantic import BaseModel
from schemas import Patient_details,result
from models import Patient
from database import get_db
import pickle

with open("Diabetes_model.pkl","rb") as file:
    model=pickle.load(file)



app=FastAPI()
@app.post("/result/{Patient_id}",response_model=result,status_code=status.HTTP_200_OK)


def predict(Patient_id:int,patient:Patient_details,db:Session=Depends(get_db)):
    new_pateint=Patient(**patient.model_dump())
    return new_pateint



