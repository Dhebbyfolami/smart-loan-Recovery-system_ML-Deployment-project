# main.py

from fastapi import FastAPI
from inference import predict

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Loan Recovery Prediction API is running!"}

@app.post("/predict")
def predict_api(payload: dict):
    try:
        result = predict(payload)
        return result
    except Exception as e:
        return {"error": str(e)}
