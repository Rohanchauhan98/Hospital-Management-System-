from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
with open('heart_disease_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Normalization function (to match your training preprocessing)
def normalize_input(age, trestbps, thalach):
    # Scale input features as the model was trained (based on your previous code)
    max_values = {
        'age': 77,          # max value for age column during training
        'trestbps': 200,    # max value for resting blood pressure
        'thalach': 202      # max value for max heart rate
    }
    
    # Normalizing the input values based on max value (as in training)
    age_norm = age / max_values['age']
    trestbps_norm = trestbps / max_values['trestbps']
    thalach_norm = thalach / max_values['thalach']
    
    return [age_norm, trestbps_norm, thalach_norm]

@app.route('/')
def home():
    return render_template('index.html')  # Ensure you have an index.html file

@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the form
    data = request.form
    age = float(data['age'])
    trestbps = float(data['trestbps'])
    thalach = float(data['thalach'])

    # Normalize the input features before passing to the model
    normalized_data = normalize_input(age, trestbps, thalach)

    # Make prediction using the model
    prediction = model.predict([normalized_data])[0]

    return jsonify({'predicted_cholesterol': prediction})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)