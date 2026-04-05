import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load the trained model
model = joblib.load('models/aqi_model.pkl')

st.set_page_config(page_title="AQI Prediction Dashboard", layout="wide")

st.title("🌬️ Air Quality Index (AQI) Predictor")
st.markdown("Enter the pollutant levels below to predict the air quality index.")

# Create two columns for inputs
col1, col2 = st.columns(2)

with col1:
    pm25 = st.slider("PM2.5 (Fine Particulate Matter)", 0.0, 500.0, 50.0)
    pm10 = st.slider("PM10 (Respirable Particulate Matter)", 0.0, 500.0, 80.0)
    no2 = st.slider("NO2 (Nitrogen Dioxide)", 0.0, 200.0, 20.0)

with col2:
    co = st.slider("CO (Carbon Monoxide)", 0.0, 50.0, 1.0)
    so2 = st.slider("SO2 (Sulphur Dioxide)", 0.0, 200.0, 15.0)
    o3 = st.slider("O3 (Ozone)", 0.0, 200.0, 30.0)

if st.button("Predict AQI"):
    # Arrange features in the same order as trained
    input_data = np.array([[pm25, pm10, no2, co, so2, o3]])
    prediction = model.predict(input_data)[0]
    
    # Determine the Category
    if prediction <= 50:
        color = "green"
        status = "Good"
    elif prediction <= 100:
        color = "yellow"
        status = "Satisfactory"
    elif prediction <= 200:
        color = "orange"
        status = "Moderate"
    else:
        color = "red"
        status = "Poor/Hazardous"

    st.metric(label="Predicted AQI Value", value=f"{prediction:.2f}")
    st.markdown(f"### Status: <span style='color:{color}'>{status}</span>", unsafe_allow_html=True)