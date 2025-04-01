import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib

# Load dataset
df = pd.read_csv("house_prices.csv")

# Define feature columns and target
X = df[['size', 'bedrooms', 'bathrooms', 'location']]  # Modify according to your dataset
y = df['price']

# Convert categorical data (location) into numerical using one-hot encoding
X = pd.get_dummies(X, columns=['location'], drop_first=True)

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# Predict on test set
y_pred = model.predict(X_test_scaled)

# Evaluate model
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"Mean Absolute Error: {mae}")
print(f"Root Mean Squared Error: {rmse}")

# Save model
joblib.dump(model, "house_price_model.pkl")
joblib.dump(scaler, "scaler.pkl")