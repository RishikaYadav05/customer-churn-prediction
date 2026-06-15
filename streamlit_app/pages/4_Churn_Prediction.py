import streamlit as st

st.title("🔮 Customer Churn Prediction")

tenure = st.slider(
    "Tenure",
    0,
    72,
    12
)

monthly_charges = st.number_input(
    "Monthly Charges",
    0.0,
    200.0,
    50.0
)

if st.button("Predict"):
    st.success(
        "Prediction functionality coming soon."
    )
