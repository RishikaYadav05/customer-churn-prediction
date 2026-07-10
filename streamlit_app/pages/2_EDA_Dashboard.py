import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

# Project root directory
BASE_DIR = Path(__file__).resolve().parents[2]

DATA_PATH = BASE_DIR / "data" / "WA_Fn-UseC_-Telco-Customer-Churn.csv"
PCA_IMAGE = BASE_DIR / "streamlit_app" / "pca_visualization.png"

df = pd.read_csv(DATA_PATH)

st.title("📈 EDA Dashboard")

fig, ax = plt.subplots(figsize=(6,4))

sns.countplot(
    x="Churn",
    data=df,
    ax=ax
)

st.pyplot(fig)

st.subheader("PCA Visualization")

st.image(PCA_IMAGE, use_container_width=True)
