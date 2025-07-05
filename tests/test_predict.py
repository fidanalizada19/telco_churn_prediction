from src.predict import predict_single

def test_predict_single():
    sample_input = {
        "Partner": "Yes",
        "Dependents": "No",
        "tenure": 24,
        "InternetService": "DSL",
        "OnlineSecurity": "Yes",
        "OnlineBackup": "No",
        "DeviceProtection": "Yes",
        "TechSupport": "No",
        "StreamingMovies": "Yes",
        "Contract": "Two year",
        "PaymentMethod": "Credit card (automatic)",
        "MonthlyCharges": 89.99
    }

    result = predict_single(sample_input)

    assert isinstance(result, dict)
    assert "prediction" in result
    assert result["prediction"] in [0, 1]
    assert "probability" in result
    assert 0.0 <= result["probability"] <= 1.0
