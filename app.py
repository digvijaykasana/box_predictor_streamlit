import streamlit as st
from utils.predictor import predict_box_counts, INPUT_CATEGORIES

st.set_page_config(page_title="📦 Box Dimension Predictor", layout="wide")

st.title("📦 Box Dimension Predictor")
st.markdown("Add multiple orders below and predict box dimensions for each.")

# Number of orders
num_orders = st.number_input("How many orders do you want to predict?", min_value=1, step=1, value=1)

# Store predictions
predictions = {}

# Collect inputs for each order
for i in range(num_orders):
    with st.expander(f"Order {i+1} - Enter Product Quantities"):
        quantities = []
        for cat in INPUT_CATEGORIES:
            qty = st.number_input(f"Order {i+1} - {cat}", key=f"{cat}_{i}", min_value=0, step=1)
            quantities.append(qty)

        if sum(quantities) == 0:
            st.warning(f"Please enter at least one non-zero quantity for Order {i+1}.")
        else:
            if st.button(f"Predict Boxes for Order {i+1}", key=f"predict_{i}"):
                prediction = predict_box_counts(INPUT_CATEGORIES, quantities)
                predictions[f"Order {i+1}"] = prediction

# Display results
for order_name, pred in predictions.items():
    st.success(f"✅ Predicted Box Counts for {order_name}:")
    for box, count in pred.items():
        st.markdown(f"- **{box}**: {count}")
