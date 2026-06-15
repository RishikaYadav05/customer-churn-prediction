import streamlit as st
import pandas as pd

results = pd.DataFrame({
    "Model":[
        "Logistic Regression",
        "Decision Tree",
        "Random Forest",
        "KNN"
    ],
    "Accuracy":[
        0.7594,
        0.7331,
        0.7828,
        0.6927
    ]
})

st.title("🏆 Model Comparison")

st.dataframe(results)

st.bar_chart(
    results.set_index("Model")
)
