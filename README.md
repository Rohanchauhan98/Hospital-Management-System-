project:
  name: "Hospital Management System — HTML, CSS, JavaScript + Cholesterol Prediction AI"
  description: >
    This project is a Hospital Management System built using HTML, CSS, JavaScript,
    and a Cholesterol Prediction AI Model integrated through a Python Flask backend.
    It allows users to interact with hospital-related pages such as doctor login,
    patient login, appointments, profiles, and dashboards, while also providing
    an AI-powered cholesterol risk prediction module.

features:
  frontend:
    description: "Hospital Management Frontend (HTML, CSS, JS)"
    type: "Static Web UI"
    pages:
      - "Doctor Login / Register"
      - "Patient Login / Register"
      - "Appointments"
      - "Doctor Profiles"
      - "Contact Page"
      - "Welcome Dashboard"

  ai_model:
    description: "Cholesterol Prediction AI Model"
    model_file: "cholesterol_model.pkl"
    functionality:
      - "Accepts patient health inputs"
      - "Predicts cholesterol risk (high/low)"
      - "Runs preprocessing and inference on backend"
    backend_usage: "Flask loads and uses the model for predictions"

  backend:
    framework: "Flask (Python)"
    main_file: "appl.py"
    responsibilities:
      - "Handles routing and page rendering"
      - "Loads the AI model"
      - "Receives form or API data"
      - "Returns predictions dynamically"
      - "Serves a simple API endpoint for model inference"
