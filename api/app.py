from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd


app = FastAPI()

# Load trained model
model = joblib.load("models/credit_risk_model.pkl")


# Get expected features from model
expected_features = model.feature_names_in_


# Accept Any Inoput

class CreditInput(BaseModel) :
    data: dict


@app.get("/")
def home():
    return { "message": "ML API Running"}

@app.post("/predict")
def predcit(payload: CreditInput):

    try:
        input_data = payload.data

        # Convert to DataFrame
        df = pd.DataFrame([input_data])

        for col in expected_features:
            if col not in df.columns:
                df[col] = 0


        df = df[expected_features]

        prediction = model.predict_proba(df)[0][1]

        return {
            "risk_score": float(prediction)
        }
    
    except Exception as e:
        return {"error": str(e)}