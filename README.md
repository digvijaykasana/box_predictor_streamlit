# Box Predictor — Streamlit UI

A Streamlit frontend for the **Optima** box‑prediction model and the **ADK agent**.

## Modes
- **Local model:** load artifacts from `./artifacts` (Optima).
- **ADK backend:** send prompts to the ADK agent and display results.

## Run
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
streamlit run streamlit_app.py     # or: streamlit run app.py
```

## .env
```
MODEL_PATH=./artifacts/model.joblib
PREPROCESS_PATH=./artifacts/preprocess.joblib
SCHEMA_PATH=./artifacts/schema.json
ADK_BASE_URL=http://127.0.0.1:8000
ADK_API_KEY=
```

## Requirements
```
streamlit
pandas
numpy
scikit-learn
xgboost
joblib
python-dotenv
requests
```
