#  Telco Churn Prediction — MLOps End-to-End Project

✨ Bu layihədə bir telekom şirkətində müştərinin **gedib-getməyəcəyini** (churn olub-olmayacağını) proqnozlaşdırırıq. Ən gözəl tərəfi? Bu, sırf bir model qurub saxlamaq deyil — bu, tam **MLOps flow**-udur. Hər şey **end-to-end** işləyir!

---

## 🔧 Texnologiyalar

| Sahə           | İstifadə Olunan Alətlər     |
|----------------|-----------------------------|
| 📊 EDA & Modelləşdirmə  | `pandas`, `scikit-learn`, `RandomForest` |
| 🧠 Drift Detection     | `scipy.stats.ks_2samp` |
| 🖥️ API                 | `FastAPI`, `joblib`, `uvicorn` |
| 📦 Containerization    | `Docker`, `Docker Compose` |
| 🌐 UI                  | `Streamlit` |
| 🗃️ Database            | `MySQL` |
| 🔍 ML Pipeline         | `Pipeline`, `OneHotEncoder`, `StandardScaler` |

---

## 📁 Layihə Strukturu

```bash
telco_churn_prediction/
├── api/                  # FastAPI backend
├── data/                 # Raw & reference data
├── models/               # Model training, drift detection
├── ui/                   # Streamlit frontend
├── tests/                # API testləri
├── docker/               # Dockerfile və s.
├── docker-compose.yml    # Multi-container orchestration
├── requirements.txt      # Python paketləri
├── README.md             
