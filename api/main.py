from fastapi import FastAPI
from pydantic import BaseModel
from src.predict import predict_single
from src.db_utils import get_db_connection, insert_prediction
from src.drift_detection import detect_drift
import pandas as pd

app = FastAPI(title="Telco Churn Predictor")
reference_df = pd.read_csv("data/reference_data.csv")

class CustomerData(BaseModel):
    Partner: str
    Dependents: str
    tenure: int
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingMovies: str
    Contract: str
    PaymentMethod: str
    MonthlyCharges: float

@app.get("/")
def root():
    return {"message": "Welcome to the Telco Churn API!"}

@app.post("/predict_telco")
def predict_churn(data: CustomerData):
    conn = get_db_connection()
    if conn is None:
        return {"error": "DB connection failed"}
    
    df = pd.DataFrame([data.dict()])
    result = predict_single(data.dict())
    prediction_label = "Stayed" if result["prediction"] == 1 else "Churned"

    drift_features = detect_drift(reference_df, df)
    insert_prediction(conn, data, prediction_label)

    return {
        "prediction": prediction_label,
        "probability": result["probability"],
        "drift_detected_in": drift_features
    }
