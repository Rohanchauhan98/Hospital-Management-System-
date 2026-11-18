# Hospital Management System

A web-based Hospital Management System built with **HTML, CSS,
JavaScript, Python, and Flask**. The project includes hospital-related
pages for doctors and patients, appointment booking, and a
machine-learning feature that predicts cholesterol-related health risk
from patient health parameters.

## Features

-   Doctor and patient login/registration interfaces
-   Appointment booking functionality
-   Doctor profile pages and hospital dashboard
-   Interactive frontend built with HTML, CSS, and JavaScript
-   Flask backend for handling routes and prediction requests
-   Machine-learning model integration using `heart_disease_model.pkl`

## Tech Stack

-   **Frontend:** HTML, CSS, JavaScript
-   **Backend:** Python, Flask
-   **Machine Learning:** Python, scikit-learn-compatible serialized
    model (see project dependencies)
-   **Model file:** `heart_disease_model.pkl`

## Run Locally

1.  **Clone the repository**

    ``` bash
    git clone https://github.com/Rohanchauhan98/Hospital-Management-System-.git
    ```

2.  **Open the project folder**

    ``` bash
    cd Hospital-Management-System-
    ```

3.  **Move into the application folder**

    ``` bash
    cd "Demo hospital"
    ```

4.  **Create and activate a virtual environment (recommended)**

    ``` bash
    python -m venv venv
    ```

    Windows:

    ``` bash
    venv\Scripts\activate
    ```

    macOS/Linux:

    ``` bash
    source venv/bin/activate
    ```

5.  **Install dependencies**

    If the project contains a `requirements.txt` file:

    ``` bash
    pip install -r requirements.txt
    ```

    If it does not, install the Python packages required by the imports
    in `appl.py` and the model code.

6.  **Start the Flask application**

    ``` bash
    python appl.py
    ```

7.  Open the local address printed in the terminal (commonly
    `http://127.0.0.1:5000/`) in your browser.

## Machine Learning Model

The application loads the trained model from `heart_disease_model.pkl`
and uses patient health parameters to generate a cholesterol-related
risk prediction. This feature is for project demonstration only and is
**not intended for medical diagnosis or treatment decisions**.

## Future Improvements

-   Add secure authentication and role-based access
-   Connect patient, doctor, and appointment data to a database
-   Add input validation and clearer error handling
-   Improve deployment and production configuration

## Author

**Rohan Chauhan**

GitHub: [@Rohanchauhan98](https://github.com/Rohanchauhan98)
