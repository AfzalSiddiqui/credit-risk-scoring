import joblib

model = joblib.load("models/credit_risk_model.pkl")

expected_features = model.feature_names_in_