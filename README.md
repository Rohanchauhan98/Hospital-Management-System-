project: "Hospital Management System"
subtitle: "HTML, CSS, JavaScript + Cholesterol Prediction AI Model"

description: >
  A web-based Hospital Management System built using HTML, CSS, and JavaScript.
  The project includes multiple hospital-related pages such as doctor login, patient login,
  registration, appointments, and profile pages. An AI-powered Cholesterol Prediction Model
  is integrated using a Python Flask backend to analyze patient health inputs and predict
  cholesterol risk.

features:
  frontend:
    title: "Frontend (HTML, CSS, JavaScript)"
    details:
      - "Doctor Login & Registration"
      - "Patient Login & Registration"
      - "Appointment Scheduling System"
      - "Doctor Profile Pages"
      - "Welcome Dashboard"
      - "Contact & Information Pages"
      - "Static, user-friendly design using pure HTML/CSS/JS"

  ai_model:
    title: "Cholesterol Prediction AI Model"
    details:
      - "ML model trained on health data and saved as a .pkl file"
      - "Predicts cholesterol-related risk from patient input"
      - "Integrated with Flask backend"
      - "Real-time prediction using form data"

  backend:
    title: "Python Flask Backend"
    details:
      - "appl.py handles routing and API communication"
      - "Loads AI model using pickle"
      - "Receives form inputs, runs prediction, returns result"
      - "Simple and efficient HTTP endpoint"

tech_stack:
  - HTML
  - CSS
  - JavaScript
  - Python
  - Flask
  - Pickle ML Model

project_structure:
  - static/: "CSS styles and static assets"
  - templates/: "All HTML page templates"
  - appl.py: "Backend + AI model integration"
  - heart_disease_model.pkl: "Cholesterol prediction AI model"
  - heart.csv: "Dataset used for training the model"

how_to_run:
  frontend:
    - "Open HTML files directly in a browser"
    - "Or use VS Code Live Server for auto-refresh preview"
  backend:
    - "Navigate to the project folder containing appl.py"
    - "Run: python appl.py"
    - "Open: http://127.0.0.1:5000"

use_case: >
  Demonstrates how a hospital management system can integrate machine learning
  for real-time medical risk prediction, combining web development and AI.

author: "Rohan Chauhan"
