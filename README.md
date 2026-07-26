# 🔋 EV Battery Health Prediction System


## Project Overview

This project predicts:

1. Battery State of Health (SOH)
2. Remaining Useful Life (RUL)

using machine learning models.


## Machine Learning Approach

Workflow:

Dataset
↓
Data Cleaning
↓
Exploratory Data Analysis
↓
Feature Engineering
↓
XGBoost Models
↓
Streamlit Deployment


## Features Used

- Cycle
- Voltage
- Temperature
- Capacity


## Models Used

### SOH Prediction
Algorithm:
XGBoost Regressor


### RUL Prediction
Algorithm:
XGBoost Regressor


## Model Performance

SOH Model:

R² Score: 0.93


RUL Model:

R² Score: 0.95


## Application

Streamlit web application allows users to enter battery parameters and get:

- Predicted SOH %
- Remaining Useful Life
- Battery Condition


## Project Structure

EV_Battery_Health_Prediction

├── app.py

├── models

├── notebooks

├── data

└── requirements.txt


## How to Run

Install dependencies:

pip install -r requirements.txt


Run application:

streamlit run app.py