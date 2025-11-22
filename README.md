title: "🏥 Hospital Management System — HTML, CSS, JavaScript + Cholesterol Prediction AI"
description: >
  A Hospital Management System built using HTML, CSS, JavaScript, and a Python-based
  Cholesterol Prediction AI model. The project provides hospital-related interfaces
  such as login pages, appointments, profiles, and integrates an ML model through
  a Flask backend for cholesterol level prediction.

features:
  frontend:
    - "Fully responsive Hospital Management UI built with HTML, CSS, and JavaScript"
    - "Doctor & Patient Login pages"
    - "Registration pages"
    - "Appointment scheduling"
    - "Doctor profile pages"
    - "Patient welcome dashboard"
    - "Contact & information pages"
  ai_model:
    - "Trained Cholesterol Prediction Machine Learning model"
    - "Model stored as a .pkl file (e.g., heart_disease_model.pkl)"
    - "Predicts patient cholesterol-related health risks"
    - "Takes health metrics as input and returns AI prediction"
  backend:
    - "Flask backend handles routing and predictions"
    - "appl.py loads the AI model and processes user input"
    - "API endpoint returns cholesterol prediction dynamically"

tech_stack:
  - HTML
  - CSS
  - JavaScript
  - Python (Flask)
  - Pickle-based ML Model (Cholesterol Prediction)

project_structure:
  - static/: "CSS and frontend assets"
  - templates/: "HTML pages"
  - appl.py: "Flask backend and model integration"
  - heart_disease_model.pkl: "Cholesterol prediction model"
  - heart.csv: "Dataset used for building the AI model"

how_to_run:
  frontend:
    - "Open HTML files directly or use Live Server (VS Code extension)."
  backend:
    - "Navigate to project folder containing appl.py"
    - "Run: python appl.py"
    - "Open browser at: http://127.0.0.1:5000"
  note: "Model will load automatically, and prediction form will route data to the backend."

use_case: >
  This project demonstrates how a hospital management interface can integrate
  AI-powered health predictions to assist doctors and patients by estimating
  cholesterol-related risk.

author: "Rohan Chauhan"
