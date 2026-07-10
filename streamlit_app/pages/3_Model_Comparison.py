import streamlit as st
import pandas as pd
from pathlib import Path

# ------------------------
# Project Base Directory
# ------------------------

BASE_DIR = Path(__file__).resolve().parents[2]

FEATURE_IMAGE = BASE_DIR / "streamlit_app" / "feature_importance.png"

# ------------------------
# Model Results
# ------------------------

results = pd.DataFrame({
    "Model": [
        "Logistic Regression",
        "Decision Tree",
        "Random Forest",
        "KNN"
    ],
    "Accuracy": [
        0.7594,
        0.7331,
        0.7828,
        0.6927
    ]
})

st.title("🏆 Model Comparison")

st.subheader("Model Accuracy")

st.dataframe(results)

st.bar_chart(
    results.set_index("Model")
)

st.subheader("Feature Importance")

st.image(
    FEATURE_IMAGE,
    use_container_width=True
)
