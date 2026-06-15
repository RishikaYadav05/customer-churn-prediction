import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(
    "../data/WA_Fn-UseC_-Telco-Customer-Churn.csv"
)

st.title("📈 EDA Dashboard")

fig, ax = plt.subplots()

sns.countplot(
    x="Churn",
    data=df,
    ax=ax
)

st.pyplot(fig)
