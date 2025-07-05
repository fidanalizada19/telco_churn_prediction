import streamlit as st
import requests

API_URL = "http://telco_api_prod:8000"
st.set_page_config(page_title="Telco Churn Predictor", page_icon="📱")

st.title("📞 Telco Churn Prediction App")
st.write("Aşağıdakı formu doldur və bu müştərinin gedib-getməyəcəyini öyrən ✨")

partner = st.selectbox("Partner", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])
tenure = st.slider("Tenure (months)", 0, 72, 12)
internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
online_security = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
online_backup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
device_protection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
streaming_movies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
payment_method = st.selectbox(
    "Payment Method",
    ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]
)
monthly_charges = st.number_input("Monthly Charges ($)", min_value=0.0, max_value=200.0, value=70.0)

# 🔮 API çağırışı
if st.button("🔮 Predict"):
    input_data = {
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly_charges
    }

    try:
        response = requests.post("http://host.docker.internal:8000/predict_telco", json=input_data)

        if response.status_code == 200:
            result = response.json()["prediction"]
            prob = response.json()["probability"]
            drift = response.json()["drift_detected_in"]

            st.success(f"✨ Proqnoz: Müştəri **{result}** olacaq.")
            st.write(f"🧠 Ehtimal: `{prob * 100:.2f}%`")
            if drift:
                st.warning(f"⚠️ Drift aşkarlanıb bu sütunlarda: {', '.join(drift)}")
        else:
            st.error("API cavab vermədi. Zəhmət olmasa backendin işlədiyindən əmin ol.")
    except Exception as e:
        st.error(f"🔌 Bağlantı xətası: {e}")
