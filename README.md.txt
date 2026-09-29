# Insurance Premium Forecasting

A Machine Learning project that predicts an individual's **Insurance Premium Category** as **Low, Medium, or High** based on personal, lifestyle, and financial information.

## Project Overview

The goal of this project is to use machine learning to estimate the insurance premium category of a person based on factors such as:

- Age
- Weight
- Height
- BMI
- Annual Income
- Smoking status
- City
- Occupation
- Other engineered lifestyle-related features

The project includes a trained ML model, a FastAPI backend for serving predictions, and a Streamlit frontend for an interactive user interface.

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- FastAPI
- Uvicorn
- Streamlit
- Joblib
- Jupyter Notebook

## Project Structure

```text
Insurance Premium Predictor/
│
├── fastapi-ml-model.ipynb   # Model development and experimentation
├── insurance.csv             # Dataset
├── model.pkl                 # Trained ML model
├── app.py                    # FastAPI backend
├── frontend.py               # Streamlit frontend
├── main.py                   # Application/backend code
├── patients.json             # Sample data
├── requirements.txt          # Project dependencies
├── .gitignore
└── README.md