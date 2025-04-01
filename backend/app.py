from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Initialize FastAPI backend
app = FastAPI()

# Load the trained model
model = joblib.load('models/tuned_fraud_detection_model.pkl')


# Define a class for the input data
class TransactionData(BaseModel):
    transaction_amount: float
    transaction_time: str
    transaction_type: str
    device: str
    location_risk: float
    # Add other features if necessary


# Initialize scaler (used during training)
scaler = StandardScaler()


# Define a function for prediction
@app.post("/predict")
async def predict(transaction: TransactionData):
    # Convert the input data into a DataFrame
    input_data = pd.DataFrame([transaction.dict()])

    # Preprocess the input data (one-hot encoding and scaling)
    input_data = pd.get_dummies(input_data, drop_first=True)

    # Make sure the input data is scaled (using the same scaler as during training)
    input_data_scaled = scaler.fit_transform(input_data)  # Or load scaler from file

    # Predict fraud or not (0 for normal, 1 for fraud)
    prediction = model.predict(input_data_scaled)

    # Return prediction result
    return {"prediction": int(prediction[0])}

