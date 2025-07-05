Welcome to **Telco Churn Predictor** 

| Layer        | Texnologiya              |
|--------------|---------------------------|
| UI           | Streamlit                |
| API          | FastAPI                  |
| ML Model     | RandomForest + sklearn   |
| DB           | MySQL                    |
| Monitoring   | Drift Detection (KS-test)|
| Container    | Docker                   |

Struktur
├── api/               # FastAPI endpointləri
├── data/              # telco.csv və reference_data.csv
├── docker/            # Dockerfile
├── envs/              # .envs.prod və .envs.test
├── models/            # final_rf_pipeline.pkl
├── notebooks/         # EDA
├── src/               # predict.py, db_utils.py, drift_detection.py
├── tests/             # test_predict, test_api
├── ui/                # Streamlit app.py
├── init.sql           # MySQL üçün schema
├── requirements.txt
└── train_model.py     # Modelin öyrədilməsi

docker-compose -f docker-compose.dev.yml up --build
localhost:8000 → FastAPI

localhost:8501 → Streamlit UI

localhost:3306 → MySQL (default root user)

Yeni gələn məlumatlar reference_data.csv ilə müqayisə edilir. Əgər statistik fərq (p < 0.1) varsa → drift detected