# mlops_fastapi_model_deployment
PredictServe - Production ML Model Deployment using FastAPI

PredictServe:
A simple end-to-end machine learning project where I trained a Logistic Regression model and deployed it using FastAPI.
The goal of this project was to understand how a model moves from a notebook into a real API that can be used in production.
Instead of keeping everything inside Jupyter, I separated:
Model training
Model saving
API serving
Basic UI for predictions

What This Project Does:
Creates a small synthetic dataset
Trains a Logistic Regression model
Saves the model as model.pkl
Loads the model inside a FastAPI app

Provides:
REST API endpoint
Simple web UI for predictions

Tech Stack:
Python
Scikit-learn
FastAPI
Uvicorn
Joblib
HTML (basic frontend inside FastAPI)
