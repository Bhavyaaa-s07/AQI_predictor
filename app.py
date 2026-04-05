import streamlit as st
import pickle
import numpy as np
import pandas as pd

# --- LOAD MODEL ---
try:
    with open('aqi_model.pkl', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("Model file 'aqi_model.pkl' not found. Run train_model.py first!")

st.set_page_config(page_title="AI AQI Pro Dashboard", layout="wide")

# --- CALLBACKS FOR YOUR FAVORITE BUTTONS ---
def set_clean_day():
    st.session_state.temp = 20
    st.session_state.wind = 35
    st.session_state.traffic = 0.1

def set_smog_day():
    st.session_state.temp = 40
    st.session_state.wind = 2
    st.session_state.traffic = 0.9

# Initialize state
if 'temp' not in st.session_state: st.session_state.temp = 28
if 'wind' not in st.session_state: st.session_state.wind = 15
if 'traffic' not in st.session_state: st.session_state.traffic = 0.4

# --- SIDEBAR ---
st.sidebar.header("🕹️ Quick Scenarios")
st.sidebar.button("🍃 Clean Windy Day", on_click=set_clean_day)
st.sidebar.button("🚗 Rush Hour Smog", on_click=set_smog_day)

st.title("🌍 Pro Environmental AQI System")
st.markdown("---")

# --- CREATE THE TABS ---
tab1, tab2 = st.tabs(["✨ Live Predictor & Health", "📈 24h Time-Series Forecast"])

with tab1:
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("⚙️ Adjust Environment")
        temp = st.slider("Temperature (°C)", 15, 45, value=st.session_state.temp)
        wind = st.slider("Wind Speed (km/h)", 0, 40, value=st.session_state.wind)
        traffic = st.slider("Traffic Density (0-1)", 0.0, 1.0, value=st.session_state.traffic)
        hour = st.number_input("Hour of Day (0-23)", 0, 23, 12)
        
        # We add dummy values for the 'lag' features so the model can run
        features = np.array([[temp, 60, wind, 10, traffic, hour, 85, 90]])
        prediction = model.predict(features)[0]

    with col2:
        st.subheader("🧠 Real-Time Inference")
        st.metric(label="Predicted AQI", value=round(prediction, 2))
        
        if prediction < 60:
            st.success("### Status: GOOD 🍃")
            st.info("**Advice:** Perfect for outdoor activities!")
        elif prediction < 120:
            st.warning("### Status: MODERATE ⚠️")
            st.write("**Advice:** Sensitive groups should limit long stays outside.")
        else:
            st.error("### Status: HAZARDOUS 😷")
            st.write("**🚨 CRITICAL PRECAUTIONS:**")
            st.markdown("* **Wear N95 Mask** | **Avoid Outdoors** | **Seal Windows**")

with tab2:
    st.subheader("🔮 Predictive Trend (Next 24 Hours)")
    
    # Simulate the next 24 hours based on the user's current 'Temp' and 'Wind'
    future_hours = np.arange(0, 24)
    forecast = []
    for h in future_hours:
        # Simulate traffic peaking during day hours
        sim_traffic = traffic * (1 + 0.2 * np.sin(2 * np.pi * (h-8)/24))
        f_point = np.array([[temp, 60, wind, 10, np.clip(sim_traffic, 0, 1), h, prediction, prediction]])
        forecast.append(model.predict(f_point)[0])
    
    chart_df = pd.DataFrame({"AQI": forecast}, index=[f"T+{h}h" for h in future_hours])
    st.line_chart(chart_df)
    st.caption("This forecast uses the current environment and projects urban traffic patterns.")

# --- FOOTER ---
st.markdown("---")
st.subheader("📊 Why this Prediction?")
importances = model.feature_importances_
f_names = ['Temp', 'Humid', 'Wind', 'Vis', 'Traffic', 'Hour', 'Lag3', 'Roll6']
imp_df = pd.DataFrame({'Feature': f_names, 'Importance': importances}).sort_values(by='Importance', ascending=False)
st.bar_chart(imp_df.set_index('Feature'))