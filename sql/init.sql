CREATE DATABASE IF NOT EXISTS telco_db;
USE telco_db;

CREATE TABLE IF NOT EXISTS telco_predictions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Partner VARCHAR(10),
    Dependents VARCHAR(10),
    tenure INT,
    InternetService VARCHAR(30),
    OnlineSecurity VARCHAR(30),
    OnlineBackup VARCHAR(30),
    DeviceProtection VARCHAR(30),
    TechSupport VARCHAR(30),
    StreamingMovies VARCHAR(30),
    Contract VARCHAR(30),
    PaymentMethod VARCHAR(50),
    MonthlyCharges FLOAT,
    Prediction VARCHAR(50)
);

