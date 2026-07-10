import streamlit as st
import pandas as pd
from pathlib import Path

# ------------------------
# Load Dataset
# ------------------------

BASE_DIR = Path(__file__).resolve().parents[2]

DATA_PATH = BASE_DIR / "data" / "WA_Fn-UseC_-Telco-Customer-Churn.csv"

df = pd.read_csv(DATA_PATH)

# ------------------------
# Dataset Overview
# ------------------------

st.title("📊 Dataset Overview")

st.write("### Dataset Shape")
st.write(df.shape)

st.write("### First 5 Rows")
st.dataframe(df.head())

st.write("### Statistical Summary")
st.dataframe(df.describe())
