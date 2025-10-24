
# 📦 Box Predictor (Streamlit App)

This project predicts how many boxes of each dimension are needed for one or more orders, based on product category quantities. It uses a pre-trained **Optuna-tuned Random Forest** model stored locally and provides an interactive **Streamlit** interface for testing on real orders.

---

## 🧠 What It Does

- Takes user input for multiple product categories and quantities.  
- Uses a feature-engineered Random Forest model (`optuna_random_forest1_model.pkl`) to predict box counts for each box dimension.  
- Shows instant results on a clean web dashboard built with Streamlit.  

Everything runs locally — no API calls, no cloud dependencies.

---

## 📂 Project Structure

```
box_predictor_streamlit/
│
├── app.py                     # Streamlit UI logic
├── requirements.txt            # Dependencies
├── model/
│   └── optuna_random_forest1_model.pkl   # Trained Random Forest model
└── utils/
    └── predictor.py            # Core logic: feature prep + prediction
```

---

## ⚙️ Setup Instructions

1. **Clone or extract the folder**
   ```bash
   git clone <repo-link>
   cd box_predictor_streamlit
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate       # Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure the model file is present**
   The model should be placed under:
   ```
   box_predictor_streamlit/model/optuna_random_forest1_model.pkl
   ```
   If you’ve retrained or tuned a new version, replace this file with the new one.

---

## 🚀 Running the App

Run Streamlit from the root directory:

```bash
streamlit run app.py
```

This opens a local web interface (usually `http://localhost:8501`).

---

## 🧩 How It Works

### 1. Feature Setup
The model uses a fixed input schema defined in `utils/predictor.py`:

```python
INPUT_CATEGORIES = [
    "Category_100cc", "Category_1100ml", "Category_12 weight|kg",
    "Category_150g", "Category_4240cc", "Category_500G",
    "Category_5lbs", "Category_710ml", "Category_8150ml",
    "Category_900ml", "Category_C box 16*12*11.5"
]
```

It also derives three key summary features:
- **Total No. of Quantity**  
- **Average Quantity per Category**  
- **Maximum Quantity**

These features form the input vector to the Random Forest model.

---

### 2. Prediction Flow

When a user submits order quantities:

- Streamlit collects numeric inputs for each product type.
- The `predict_box_counts()` function builds a structured feature vector.
- The trained Random Forest model (`optuna_random_forest1_model.pkl`) predicts the expected number of boxes for each size.
- Results appear as readable labels (box dimensions like `30x30x29`, `40x30x34`, etc.) with counts.

---

### 3. Streamlit Interface

The interface allows multiple orders in one go:
- You specify how many orders to predict.
- Each order expands into its own section for category-wise quantity entry.
- Predictions show up inline once you click “Predict Boxes”.

---

## 🧮 Model Notes

The saved model was trained and tuned using **Optuna** for hyperparameter optimization.  
It’s a multi-output Random Forest regressor — each output corresponds to a different box dimension.

To retrain:
1. Prepare your dataset (rows = orders, columns = quantities per category + target box counts).  
2. Train with Optuna-tuned hyperparameters.
3. Save with:
   ```python
   import joblib
   joblib.dump(model, "model/optuna_random_forest1_model.pkl")
   ```

The Streamlit app automatically loads the latest `.pkl` from the `model` directory.

---

## 🧾 Requirements

```
streamlit
scikit-learn
pandas
numpy
joblib
```

---

## 🧠 Quick Start Summary

```bash
# 1. Setup
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 2. Run
streamlit run app.py

# 3. Predict
Open browser → enter product quantities → click Predict
```

---

## ✅ Key Files to Note

| File | Purpose |
|------|----------|
| `app.py` | Front-end logic for Streamlit interface |
| `utils/predictor.py` | Loads model, prepares features, runs predictions |
| `requirements.txt` | Dependency list |
| `model/optuna_random_forest1_model.pkl` | Trained model file |

---

## 🧭 Optional Improvements

- Add input validation and default category templates.  
- Display predicted box counts as a table or chart.  
- Extend for new product categories or model types (e.g., XGBoost).  
