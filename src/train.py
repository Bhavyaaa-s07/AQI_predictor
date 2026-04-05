import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib
import os

def train_model():
    # Load dataset
    df = pd.read_csv('data/city_day.csv')
    
    # Selecting the most important features for AQI
    features = ['PM2.5', 'PM10', 'NO2', 'CO', 'SO2', 'O3']
    target = 'AQI'
    
    # 1. Handling missing values (Important for this dataset)
    # We drop rows where AQI or key features are missing
    df = df.dropna(subset=[target] + features)
    
    X = df[features]
    y = df[target]
    
    # 2. Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 3. Train Model
    print("Training the Random Forest model...")
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # 4. Save Model
    if not os.path.exists('models'):
        os.makedirs('models')
    joblib.dump(model, 'models/aqi_model.pkl')
    
    print(f"Model trained successfully! Accuracy (R2 Score): {model.score(X_test, y_test):.4f}")

if __name__ == "__main__":
    train_model()