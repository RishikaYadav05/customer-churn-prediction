import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parents[2]

# Dataset path
DATA_PATH = BASE_DIR / "data" / "WA_Fn-UseC_-Telco-Customer-Churn.csv"

# PCA image path
PCA_IMAGE = BASE_DIR / "streamlit_app" / "pca_visualization.png"

# Load dataset
df = pd.read_csv(DATA_PATH)

st.title("📈 EDA Dashboard")

# Churn Distribution
fig, ax = plt.subplots(figsize=(6, 4))
sns.countplot(x="Churn", data=df, ax=ax)
ax.set_title("Customer Churn Distribution")
st.pyplot(fig)

# PCA Visualization
st.subheader("PCA Visualization")
st.image(PCA_IMAGE, use_container_width=True)
