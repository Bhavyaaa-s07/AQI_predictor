import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import pickle

# 1. Setup Synthetic Data (1000 samples)
np.random.seed(42)
n = 1000

data = {
    'temp': np.random.uniform(15, 45, n),
    'humidity': np.random.uniform(30, 90, n),
    'wind_speed': np.random.uniform(0, 40, n),
    'visibility': np.random.uniform(2, 20, n),
    'traffic_density': np.random.uniform(0, 1, n),
    'hour': np.random.randint(0, 24, n),
    'aqi_lag_3h': np.random.uniform(20, 300, n),   # The "Past" data
    'aqi_rolling_6h': np.random.uniform(20, 300, n) # The "Trend" data
}

df = pd.DataFrame(data)

# 2. Logic: AQI increases with Traffic/Temp/Lag, decreases with Wind
# This is the "Learning Pattern" for the AI
y = (df['traffic_density'] * 120) + (df['temp'] * 1.5) - (df['wind_speed'] * 2.5) + (df['aqi_lag_3h'] * 0.2) + 40
y = np.clip(y, 20, 500)

# 3. Train the Forest
X = df # Using all 8 columns
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# 4. Save the "Brain"
with open('aqi_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ 8-Feature Time-Series Model Saved successfully!")