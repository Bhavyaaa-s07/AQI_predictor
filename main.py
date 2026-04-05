from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(title="AQI Prediction API", description="FastAPI-based ML model serving for Air Quality Index")

# Load your model
model = joblib.load("models/aqi_model.pkl")

class AQIInput(BaseModel):
    # Adjust these names to match your specific AQI features (e.g., PM2.5, Humidity, Temp)
    features: list

@app.get("/health")
def health_check():
    return {"status": "Healthy"}

@app.get("/")
def root():
    return {"message": "Welcome to the AQI Predictor API"}

@app.post("/predict")
def predict(data: AQIInput):
    input_data = np.array(data.features).reshape(1, -1)
    prediction = model.predict(input_data)
    return {"AQI_Prediction": float(prediction[0])}