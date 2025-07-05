import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DB")
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Database connection failed: {err}")
        return None

def insert_prediction(conn, data, result):
    insert_query = """
        INSERT INTO telco_predictions 
        (Partner, Dependents, tenure, InternetService, OnlineSecurity, OnlineBackup, 
         DeviceProtection, TechSupport, StreamingMovies, Contract, PaymentMethod, 
         MonthlyCharges, Prediction)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        data.Partner, data.Dependents, data.tenure, data.InternetService,
        data.OnlineSecurity, data.OnlineBackup, data.DeviceProtection,
        data.TechSupport, data.StreamingMovies, data.Contract, data.PaymentMethod,
        data.MonthlyCharges, result
    )
    cursor = conn.cursor()
    cursor.execute(insert_query, values)
    conn.commit()
