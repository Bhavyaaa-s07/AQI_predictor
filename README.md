# 🌍 AI-Powered Environmental AQI Forecaster (v3.0)

![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue)
![ML](https://img.shields.io/badge/ML-Random_Forest-orange)

An end-to-end MLOps project that predicts the Air Quality Index (AQI) using Machine Learning, containerized with Docker, and visualized through a real-time forecasting dashboard.

---

## ⛓️ MLOps Workflow & Pipeline
This project demonstrates a full **CI/CD Pipeline** for Machine Learning:

1.  **Data Engineering:** Synthetic generation of environmental features (Temp, Wind, Traffic).
2.  **Feature Engineering:** Implementation of **3h Lag Features** and **6h Rolling Averages** to capture temporal patterns.
3.  **Model Training:** A `RandomForestRegressor` ensemble ($n=100$) trained to understand non-linear environmental interactions.
4.  **Containerization:** Environment parity achieved via **Docker**, ensuring the model runs identically on Azure, AWS, or Localhost.
5.  **Automated Inference:** A **Streamlit** dashboard serving the model via a containerized web interface.




---
## ⛓️ CI/CD & Automation Workflow
This project uses **GitHub Actions** and **Docker Hub** to automate the lifecycle:
1. **Push:** Code is pushed to GitHub.
2. **Test:** Automated scripts verify the `aqi_model.pkl` integrity.
3. **Build:** GitHub Actions triggers a `docker build`.
4. **Deploy:** The image is pushed to the registry for cloud deployment.

---

## ✨ Key Features
* **Live Predictor:** Instant AQI results based on current weather and traffic density.
* **Health Advisory System:** Dynamic medical precautions (e.g., N95 mask alerts) based on hazard levels.
* **24h Time-Series Forecast:** Predictive trend analysis using periodic traffic simulation.
* **Explainable AI (XAI):** Real-time **Feature Importance** charts showing exactly *why* the AI made a specific prediction.

---

## 🛠️ Tech Stack
* **Language:** Python 3.11
* **ML Libraries:** Scikit-Learn, NumPy, Pandas
* **Interface:** Streamlit
* **DevOps/Deployment:** Docker, GitHub Actions, Azure Container Registry

---

## 📦 How to Run

### **Option 1: Using Docker (Recommended)**
```bash
# Build the image
docker build --no-cache -t aqi-predictor-v3 .

# Run the container
docker run -p 5050:5050 aqi-predictor-v3