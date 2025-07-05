import os
import joblib
import pandas as pd

MODEL_PATH = os.path.join("models", "final_rf_pipeline.pkl")

def load_model():
    return joblib.load(MODEL_PATH)

def predict_single(input_data: dict):
    model = load_model()
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]
    return {
        "prediction": int(prediction),
        "probability": round(float(probability), 4)
    }
if __name__ == "__main__":
    sample = {
        "Partner": "Yes",
        "Dependents": "No",
        "tenure": 12,
        "InternetService": "Fiber optic",
        "OnlineSecurity": "No",
        "OnlineBackup": "Yes",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingMovies": "Yes",
        "Contract": "Month-to-month",
        "PaymentMethod": "Electronic check",
        "MonthlyCharges": 70.35
    }
    result = predict_single(sample)
    print(result)
