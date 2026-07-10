import streamlit as st
import pandas as pd
from pathlib import Path

# Project root directory
BASE_DIR = Path(__file__).resolve().parents[2]

DATA_PATH = BASE_DIR / "data" / "WA_Fn-UseC_-Telco-Customer-Churn.csv"

df = pd.read_csv(DATA_PATH)

st.title("📊 Dataset Overview")

st.subheader("Dataset Shape")
st.write(df.shape)

st.subheader("First 5 Rows")
st.dataframe(df.head())

st.subheader("Statistical Summary")
st.dataframe(df.describe())
