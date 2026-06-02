from fastapi import FastAPI
import logging
from api.schemas import CreditInput, CreditResponse
from api.services import run_prediction
from api.database import conn

logging.basicConfig(level=logging.INFO)

app = FastAPI()


@app.get("/")
def home():
    return {"message": "ML API Running"}


@app.post("/predict")
def predict(payload: CreditInput):
    try:
        input_data = payload.dict()
        result = run_prediction(input_data)
        return CreditResponse(**result)

    except Exception as e:
        import traceback
        return {
            "error": str(e),
            "trace": traceback.format_exc()
        }
    

@app.get("/predictions")
def get_predictions():

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM predictions")

    rows = cursor.fetchall()

    return rows