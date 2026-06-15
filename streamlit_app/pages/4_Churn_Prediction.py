import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("../models/random_forest_model.pkl")

st.title("🔮 Customer Churn Prediction")

gender = st.selectbox("Gender", [0, 1])

senior = st.selectbox("Senior Citizen", [0, 1])

partner = st.selectbox("Partner", [0, 1])

dependents = st.selectbox("Dependents", [0, 1])

tenure = st.slider("Tenure", 0, 72, 12)

phone_service = st.selectbox("Phone Service", [0, 1])

multiple_lines = st.selectbox("Multiple Lines", [0, 1, 2])

internet_service = st.selectbox("Internet Service", [0, 1, 2])

online_security = st.selectbox("Online Security", [0, 1, 2])

online_backup = st.selectbox("Online Backup", [0, 1, 2])

device_protection = st.selectbox("Device Protection", [0, 1, 2])

tech_support = st.selectbox("Tech Support", [0, 1, 2])

streaming_tv = st.selectbox("Streaming TV", [0, 1, 2])

streaming_movies = st.selectbox("Streaming Movies", [0, 1, 2])

contract = st.selectbox("Contract", [0, 1, 2])

paperless = st.selectbox("Paperless Billing", [0, 1])

payment = st.selectbox("Payment Method", [0, 1, 2, 3])

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

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("🔴 Customer Likely To Churn")
    else:
        st.success("🟢 Customer Likely To Stay")
