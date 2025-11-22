# Cholesterol Prediction — Web Project (HTML, CSS, JS) + AI Model

A lightweight web project with a clean **HTML / CSS / JavaScript** frontend and a simple **Python + Flask** backend that loads a trained machine-learning model to predict cholesterol risk from user inputs.

![Project UI](/mnt/data/0c0c1dc1-ed9d-4d3f-a162-8da76f1a673e.png)

---

## What this project is
- Frontend: static HTML pages, CSS styles, and client-side JavaScript for UI interactions and form validation.  
- Backend: small Flask server that receives form data, loads a saved ML model (`*.pkl`), runs preprocessing, and returns predictions.  
- Model: a trained cholesterol-prediction model saved as a pickle file (e.g. `cholesterol_model.pkl`).

---

## Features
- Clean responsive UI for entering health metrics (age, BP, cholesterol, etc.)  
- Client-side validation and UX polish with JavaScript  
- Server-side preprocessing + model inference (returns risk classification or score)  
- Option to save/log results (extendable to a DB)

---
