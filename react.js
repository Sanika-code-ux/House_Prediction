# Load model and scaler
model = joblib.load("house_price_model.pkl")
scaler = joblib.load("scaler.pkl")

# Example input (modify as needed)
new_house = pd.DataFrame({'size': [2000], 'bedrooms': [3], 'bathrooms': [2], 'location': ['Downtown']})

# Convert categorical values
new_house = pd.get_dummies(new_house, columns=['location'], drop_first=True)

# Ensure same column format as training data
missing_cols = set(X.columns) - set(new_house.columns)
for col in missing_cols:
    new_house[col] = 0

# Scale input
new_house_scaled = scaler.transform(new_house)

# Predict price
predicted_price = model.predict(new_house_scaled)
print(f"Predicted House Price: ${predicted_price[0]:,.2f}")