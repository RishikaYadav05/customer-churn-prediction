import streamlit as st
import pandas as pd

df = pd.read_csv(
    "../data/WA_Fn-UseC_-Telco-Customer-Churn.csv"
)

st.title("📊 Dataset Overview")

st.write("Dataset Shape")

st.write(df.shape)

st.write("First 5 Rows")

st.dataframe(df.head())

st.write("Statistical Summary")

st.dataframe(df.describe())
