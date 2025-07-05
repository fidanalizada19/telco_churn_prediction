from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_predict_telco():
    sample_input = {
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

    response = client.post("/predict_telco", json=sample_input)
    assert response.status_code == 200
    json_data = response.json()
    assert "prediction" in json_data
    assert json_data["prediction"] in ["Stayed", "Churned"]
    assert "drift_detected_in" in json_data
