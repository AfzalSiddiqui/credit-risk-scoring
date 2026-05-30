from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)


app = FastAPI()

# Load trained model
model = joblib.load("models/credit_risk_model.pkl")


# Get expected features from model
expected_features = model.feature_names_in_


# Accept Any Inoput

class CreditInput(BaseModel) :
    age: float
    DebtRatio: float
    MonthlyIncome: float
    NumberOfDependents: float



def run_prediction(df):
    return model.predict_proba(df)[0][1]

@app.get("/")
def home():
    return { "message": "ML API Running"}


@app.post("/predict")
def predict(payload: CreditInput):

    try:
        input_data = payload.dict()

        logging.info(f"Input: {input_data}")


        # Convert to DataFrame
        df = pd.DataFrame([input_data])

        for col in expected_features:
            if col not in df.columns:
                df[col] = 0


        df = df[expected_features]

        prediction = run_prediction(df)


        return {
            "risk_score": float(prediction)
        }
    
    except Exception as e:
        return {"error": str(e)}