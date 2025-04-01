@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from form
        size = float(request.form['size'])
        bedrooms = int(request.form['bedrooms'])
        bathrooms = int(request.form['bathrooms'])
        location = request.form['location']

        print("Received input:", size, bedrooms, bathrooms, location)  # Debugging

        # Prepare data for prediction
        input_data = pd.DataFrame({'size': [size], 'bedrooms': [bedrooms], 'bathrooms': [bathrooms], 'location': [location]})

        # Convert categorical values
        input_data = pd.get_dummies(input_data, columns=['location'], drop_first=True)

        # Ensure the input data has the same columns as the model
        missing_cols = set(model.feature_names_in_) - set(input_data.columns)
        for col in missing_cols:
            input_data[col] = 0

        print("Processed input data:", input_data)  # Debugging

        # Scale data
        input_scaled = scaler.transform(input_data)

        print("Scaled input data:", input_scaled)  # Debugging

        # Make prediction
        predicted_price = model.predict(input_scaled)[0]

        print("Predicted price:", predicted_price)  # Debugging

        return jsonify({'predicted_price': f"${predicted_price:,.2f}"})

    except Exception as e:
        print("Error:", str(e))  # Print error to console
        return jsonify({'error': str(e)})