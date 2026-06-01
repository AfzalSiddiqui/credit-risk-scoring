import pandas as pd
from model import model, expected_features


def get_risk_level(score: float):
    if score >= 0.7:
        return "HIGH", "REJECT"
    elif score >= 0.3:
        return "MEDIUM", "REVIEW"
    else:
        return "LOW", "APPROVE"


def run_prediction(input_data: dict):

    df = pd.DataFrame([input_data])

    # Align features
    for col in expected_features:
        if col not in df.columns:
            df[col] = 0

    df = df[expected_features]

    score = model.predict_proba(df)[0][1]

    risk_level, decision = get_risk_level(score)

    return {
        "risk_score": float(score),
        "risk_level": risk_level,
        "decision": decision
    }