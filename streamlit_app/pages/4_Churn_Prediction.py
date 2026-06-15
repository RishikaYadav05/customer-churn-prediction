import streamlit as st
import pandas as pd
import pickle
from pathlib import Path

# ------------------------
# Load Model and Scaler
# ------------------------

BASE_DIR = Path(__file__).resolve().parents[2]

MODEL_PATH = BASE_DIR / "models" / "random_forest_model.pkl"
SCALER_PATH = BASE_DIR / "models" / "scaler.pkl"

with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)

with open(SCALER_PATH, "rb") as file:
    scaler = pickle.load(file)

st.title("🔮 Customer Churn Prediction")

st.write("Enter customer details below:")

# ------------------------
# Customer Information
# ------------------------

gender_text = st.selectbox(
    "Gender",
    ["Female", "Male"]
)
gender = 0 if gender_text == "Female" else 1

senior_text = st.selectbox(
    "Senior Citizen",
    ["No", "Yes"]
)
senior = 0 if senior_text == "No" else 1

partner_text = st.selectbox(
    "Partner",
    ["No", "Yes"]
)
partner = 0 if partner_text == "No" else 1

dependents_text = st.selectbox(
    "Dependents",
    ["No", "Yes"]
)
dependents = 0 if dependents_text == "No" else 1

# ------------------------
# Service Details
# ------------------------

tenure = st.slider(
    "Tenure (Months)",
    min_value=0,
    max_value=72,
    value=12
)

phone_text = st.selectbox(
    "Phone Service",
    ["No", "Yes"]
)
phone_service = 0 if phone_text == "No" else 1

multiple_lines = st.selectbox(
    "Multiple Lines (Encoded)",
    [0, 1, 2]
)

internet_service = st.selectbox(
    "Internet Service (Encoded)",
    [0, 1, 2]
)

online_security = st.selectbox(
    "Online Security (Encoded)",
    [0, 1, 2]
)

online_backup = st.selectbox(
    "Online Backup (Encoded)",
    [0, 1, 2]
)

device_protection = st.selectbox(
    "Device Protection (Encoded)",
    [0, 1, 2]
)

tech_support = st.selectbox(
    "Tech Support (Encoded)",
    [0, 1, 2]
)

streaming_tv = st.selectbox(
    "Streaming TV (Encoded)",
    [0, 1, 2]
)

streaming_movies = st.selectbox(
    "Streaming Movies (Encoded)",
    [0, 1, 2]
)

# ------------------------
# Billing Details
# ------------------------

contract_text = st.selectbox(
    "Contract Type",
    [
        "Month-to-Month",
        "One Year",
        "Two Year"
    ]
)

contract_map = {
    "Month-to-Month": 0,
    "One Year": 1,
    "Two Year": 2
}

contract = contract_map[contract_text]

paperless_text = st.selectbox(
    "Paperless Billing",
    ["No", "Yes"]
)

paperless = 0 if paperless_text == "No" else 1

payment = st.selectbox(
    "Payment Method (Encoded)",
    [0, 1, 2, 3]
)

monthly = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    max_value=200.0,
    value=70.0
)

total = st.number_input(
    "Total Charges",
    min_value=0.0,
    value=1000.0
)

# ------------------------
# Prediction
# ------------------------

if st.button("Predict Churn"):

    input_data = pd.DataFrame([[
        gender,
        senior,
        partner,
        dependents,
        tenure,
        phone_service,
        multiple_lines,
        internet_service,
        online_security,
        online_backup,
        device_protection,
        tech_support,
        streaming_tv,
        streaming_movies,
        contract,
        paperless,
        payment,
        monthly,
        total
    ]], columns=[
        'gender',
        'SeniorCitizen',
        'Partner',
        'Dependents',
        'tenure',
        'PhoneService',
        'MultipleLines',
        'InternetService',
        'OnlineSecurity',
        'OnlineBackup',
        'DeviceProtection',
        'TechSupport',
        'StreamingTV',
        'StreamingMovies',
        'Contract',
        'PaperlessBilling',
        'PaymentMethod',
        'MonthlyCharges',
        'TotalCharges'
    ])

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.error("🔴 Customer Likely To Churn")
        st.warning(
            "Retention actions are recommended for this customer."
        )
    else:
        st.success("🟢 Customer Likely To Stay")
        st.info(
            "This customer is likely to remain with the company."
        )
