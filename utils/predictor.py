import joblib
import numpy as np
import os

# Load model
model_path = os.path.join("model", "optuna_random_forest1_model.pkl")
model = joblib.load(model_path)

# Define inputs and output structure
INPUT_CATEGORIES = [
    "Category_100cc", "Category_1100ml", "Category_12 weight|kg", "Category_150g",
    "Category_4240cc", "Category_500G", "Category_5lbs", "Category_710ml",
    "Category_8150ml", "Category_900ml", "Category_C box 16*12*11.5"
]

BOX_DIMENSIONS = [
    "10x10x10", "12x18x10", "12x8x20", "18x17x27", "20x20x34",
    "30x30x29", "32x20x17", "38x30x20", "40x30x29", "40x30x34",
    "40x40x34", "42x42x30", "48x34x27", "60x30x30", "8x22x13", "8x8x13"
]

ALL_FEATURES = [
    "Total No. Of Quantity",
    "Avg Quantity",
    "Max Quantity"
] + INPUT_CATEGORIES

def predict_box_counts(categories, quantities):
    # Initialize feature dict
    data = dict.fromkeys(ALL_FEATURES, 0)

    # Fill actual quantities
    for cat, qty in zip(categories, quantities):
        if cat in INPUT_CATEGORIES:
            data[cat] = qty

    total_qty = sum(quantities)
    data["Total No. Of Quantity"] = total_qty
    data["Avg Quantity"] = total_qty / len(quantities)
    data["Max Quantity"] = max(quantities)

    # Convert to model input
    input_array = np.array([[data[feature] for feature in ALL_FEATURES]])
    prediction = model.predict(input_array)[0]

    # Prepare output as a readable dict
    return {box: int(round(val)) for box, val in zip(BOX_DIMENSIONS, prediction)}
