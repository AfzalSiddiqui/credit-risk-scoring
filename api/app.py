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


@app.post("/predict", response_model=CreditResponse)
def predict(payload: CreditInput):

    logging.info(f"Input: {payload.dict()}")

    result = run_prediction(payload.dict())

    return result

@app.get("/predictions")
def get_predictions():

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM predictions")

    rows = cursor.fetchall()

    return rows