# Bangalore Home Price Prediction

A web application to predict home prices in Bangalore using machine learning. The project includes a Python backend (Flask), a trained model, and a simple HTML frontend for user interaction.

---
## Project Structure

```
BHP/
├── Client/
│   └── index.html                # Frontend HTML file
├── Model/
│   ├── banglore_home_prices_model.pickle  # Trained ML model
│   ├── Bengaluru_House_Data.csv           # Dataset
│   ├── code.ipynb                         # Jupyter notebook for training
│   └── columns.json                       # Model columns metadata
├── Server/
│   ├── server.py                  # Flask backend server
│   ├── util.py                    # Utility functions
│   └── artifacts/                 # Model and columns for backend
│       ├── banglore_home_prices_model.pickle
│       └── columns.json
├── requirements.txt               # Python dependencies
├── start_project.py               # Script to launch backend & frontend
└── README.md                      # Project documentation
```

---

## Features
- Predict home prices in Bangalore based on location, square footage, BHK, and bathrooms
- Interactive web frontend for easy testing
- REST API endpoints for integration
- Automated startup script for backend and frontend

---

## Setup Instructions

### 1. Install Python dependencies

```sh
pip install -r requirements.txt
```

### 2. Start the project (backend & frontend)

```sh
python start_project.py
```
- This will start the Flask backend and a local web server for the frontend.
- The frontend will open automatically in your default browser.

### 3. Manual startup (optional)
- To run the backend only:
  ```sh
  cd Server
  python server.py
  ```
- To run the frontend only:
  ```sh
  cd Client
  python3 -m http.server 8000
  # Then open http://localhost:8000/index.html in your browser
  ```

---

## API Endpoints

### `/get_location_names` (GET)
Returns a list of available locations.

### `/predict_home_price` (POST)
Predicts the home price. Requires form data:
- `location` (string)
- `total_sqft` (float)
- `bhk` (int)
- `bath` (int)

Returns:
- `estimated_price` (float, in Lakhs)

---

## Frontend Usage
- Fill in the location, total square feet, BHK, and bath fields.
- Click "Predict Price" to get the estimated price.

---

## Model Training
- The Jupyter notebook in `Model/code.ipynb` contains code for data analysis and model training.
- The trained model and columns metadata are saved in `Model/` and copied to `Server/artifacts/` for backend use.

---

## Notes
- Ensure Python 3.9+ is installed.
- If you retrain the model, update the files in `Server/artifacts/`.

---


