from fastapi import FastAPI
from pydantic import BaseModel


app=FastAPI()
@app.get("/")
def predict():
    return {
        "Project":"Diabetes",
        "model_saved": "pkl_file"
    }
