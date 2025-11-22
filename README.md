🏥 Hospital Management System
HTML • CSS • JavaScript • Flask • Cholesterol Prediction AI Model

A complete Hospital Management System built using HTML, CSS, JavaScript, and a Cholesterol Prediction AI Model integrated through a Python Flask backend.
This project combines a static web interface with a machine-learning model to predict cholesterol-related health risks.

🚀 Features
🖥️ Frontend (HTML, CSS, JavaScript)

Clean and responsive UI

Multiple hospital-related pages including:

Doctor Login / Register

Patient Login / Register

Appointment Booking

Doctor Profile Pages

Contact & Main Dashboard

Fully client-side interactions using JavaScript

Organized using /static and /templates folders

🧠 Cholesterol Prediction AI Model

Trained ML model saved as heart_disease_model.pkl

Takes patient health parameters (Age, BP, Thalach, etc.)

Predicts cholesterol-related health risk

Uses pickle to load the model

Integrated via API in Flask backend

⚙️ Backend (Flask + Python)

appl.py handles:

Routing

Reading input from frontend

Loading ML model

Returning prediction results

Simple and scalable API structure
