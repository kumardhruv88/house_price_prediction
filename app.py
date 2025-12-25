from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load model and scaler
try:
    with open('rf_model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
except Exception as e:
    print(f"Error loading model files: {e}")
    model = None
    scaler = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None or scaler is None:
        return jsonify({'error': 'Model not loaded.'}), 500

    try:
        data = request.get_json()
        
        # Extract features ensuring correct order
        # ['Square_Footage', 'Num_Bedrooms', 'Num_Bathrooms', 'Year_Built', 'Lot_Size', 'Garage_Size', 'Neighborhood_Quality']
        
        input_data = pd.DataFrame([{
            'Square_Footage': float(data.get('Square_Footage')),
            'Num_Bedrooms': float(data.get('Num_Bedrooms')),
            'Num_Bathrooms': float(data.get('Num_Bathrooms')),
            'Year_Built': float(data.get('Year_Built')),
            'Lot_Size': float(data.get('Lot_Size')),
            'Garage_Size': float(data.get('Garage_Size')),
            'Neighborhood_Quality': float(data.get('Neighborhood_Quality'))
        }])

        # Scale data
        scaled_data = scaler.transform(input_data)
        
        # Predict
        prediction = model.predict(scaled_data)[0]
        
        return jsonify({'prediction': f"${prediction:,.2f}"})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
