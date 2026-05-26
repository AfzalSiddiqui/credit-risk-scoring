from fastapi import FastAPI
from pydantic import BaseModel

import joblib
import pandas as pd


app = FastAPI()

# Load trained model
model = joblib.load("models/credit_risk_model.pkl")


class CreditInput(BaseModel):
    NumberOfOpenCreditLinesAndLoans: float
    NumberOfTimes90DaysLate: float
    NumberRealEstateLoansOrLines: float
    # ... ALL columns

    


@app.get("/")
def home():
    return {"message": "ML API Running"}


@app.post("/predict")
def predict(data: CreditInput):
    try:
       df = pd.DataFrame([data.dict()])

        prediction = model.predict_proba(df)[0][1]

        return {"risk_score": float(prediction)}
    
    pd.DataFrame([data.dict()])

    except Exception as e:
        return {"error": str(e)}

    # Convert validated input → dataframe
    df = pd.DataFrame([[data.age, data.DebtRatio, data.MonthlyIncome, data.NumberOfDependents]],
                  columns=["age", "DebtRatio", "MonthlyIncome", "NumberOfDependents"])
    
    # Prediction
    prediction = model.predict_proba(df)[0][1]

    return {
        "risk_score": float(prediction)
    }