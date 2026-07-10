# 📊 Customer Churn Prediction System

An end-to-end **Machine Learning** web application that predicts whether a telecom customer is likely to churn. The application helps businesses identify customers at risk of leaving and enables proactive customer retention through data-driven insights.

The prediction engine uses a **Random Forest Classifier** trained on the **IBM Telco Customer Churn Dataset**, providing accurate churn predictions based on customer demographics, subscribed services, contract details, and billing information.

---

## 🚀 Features

### 🔮 Customer Churn Prediction
- Predict whether a customer is likely to **Stay** or **Churn**.
- Interactive prediction interface built with Streamlit.
- Real-time prediction using a trained Random Forest model.

### 📊 Dataset Overview
- Display dataset dimensions.
- View first five records.
- Display statistical summary of the dataset.

### 📈 Exploratory Data Analysis (EDA)
- Churn distribution visualization.
- Data exploration using Seaborn and Matplotlib.

### 📉 PCA Visualization
- Visualize the dataset using Principal Component Analysis (PCA).
- Understand feature variance and customer distribution.

### 🏆 Model Comparison
Compare the performance of multiple machine learning models:
- Logistic Regression
- Decision Tree
- Random Forest
- K-Nearest Neighbors (KNN)

### 💡 Business Insights
Business recommendations generated from churn analysis, including:
- Focus on customers with low tenure.
- Encourage long-term contracts.
- Monitor customers with high monthly charges.
- Reward loyal customers.
- Create targeted retention campaigns.

---

# 🛠 Tech Stack

| Layer | Technology |
|--------|------------|
| Programming Language | Python |
| Machine Learning | Scikit-learn |
| Data Processing | Pandas, NumPy |
| Data Visualization | Matplotlib, Seaborn |
| Web Framework | Streamlit |
| Model Serialization | Pickle |
| Version Control | Git & GitHub |

---

# 🤖 Machine Learning Pipeline

- Data Cleaning
- Missing Value Handling
- Label Encoding
- Feature Engineering
- Min-Max Feature Scaling
- SMOTE for Class Balancing
- Model Training
- Model Evaluation
- Streamlit Deployment

---

# 🧠 Machine Learning Models

| Model | Accuracy |
|--------|----------|
| Logistic Regression | **75.94%** |
| Decision Tree | **73.31%** |
| Random Forest | **78.28%** ⭐ |
| KNN | **69.27%** |

The **Random Forest Classifier** achieved the highest accuracy and was selected as the final deployed model.

---

# 📌 Features Used

The model uses **19 input features**:

- Gender
- Senior Citizen
- Partner
- Dependents
- Tenure
- Phone Service
- Multiple Lines
- Internet Service
- Online Security
- Online Backup
- Device Protection
- Tech Support
- Streaming TV
- Streaming Movies
- Contract
- Paperless Billing
- Payment Method
- Monthly Charges
- Total Charges

---

# 📂 Project Structure

```text
customer-churn-prediction/
│
├── data/
│   ├── WA_Fn-UseC_-Telco-Customer-Churn.csv
│
├── models/
│   ├── random_forest_model.pkl
│   ├── scaler.pkl
│
├── notebooks/
│   └── Customer_Churn_Prediction.ipynb
│
├── streamlit_app/
│   ├── app.py
│   ├── pca_visualization.png
│   ├── feature_importance.png
│   └── pages/
│       ├── 1_Dataset_Overview.py
│       ├── 2_EDA_Dashboard.py
│       ├── 3_Model_Comparison.py
│       ├── 4_Churn_Prediction.py
│       └── 5_Business_Insights.py
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation & Setup

## Prerequisites

- Python 3.10 or above
- Git

---

## Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/customer-churn-prediction.git

cd customer-churn-prediction
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
cd streamlit_app

streamlit run app.py
```

---

## Open in Browser

```
http://localhost:8501
```

---

# 📊 Dataset

**Dataset Name:** IBM Telco Customer Churn Dataset

Dataset contains:

- 7,043 Customer Records
- 20 Features
- Target Variable: **Churn**

Target Labels:

- Yes → Customer Churned
- No → Customer Stayed

---

# 📈 Exploratory Data Analysis

The application includes:

- Customer Churn Distribution
- PCA Visualization
- Dataset Summary
- Statistical Analysis

---

# 📉 Model Evaluation

The Random Forest model achieved:

| Metric | Score |
|---------|-------|
| Accuracy | **78.28%** |
| Precision | **85% (Non-Churn)** |
| Recall | **85% (Non-Churn)** |
| Precision | **59% (Churn)** |
| Recall | **59% (Churn)** |

---

# 💡 Business Recommendations

Based on churn analysis, the following retention strategies are recommended:

- Improve customer engagement during the initial months.
- Encourage customers to choose long-term contracts.
- Provide loyalty rewards for long-term customers.
- Monitor customers with higher monthly charges.
- Launch targeted retention campaigns for customers with high churn probability.

---

# 🌐 Deployment

The application is deployed using **Streamlit Community Cloud**.

To deploy:

1. Push the repository to GitHub.
2. Connect the repository to Streamlit Community Cloud.
3. Select the main file:

```text
streamlit_app/app.py
```

4. Deploy the application.

---

# 📦 Requirements

Main Python libraries used:

```text
streamlit
pandas
numpy
matplotlib
seaborn
scikit-learn
imbalanced-learn
pickle
```

---

# 📸 Screenshots

### Home Page

_Add screenshot here_

### Dataset Overview

_Add screenshot here_

### EDA Dashboard

_Add screenshot here_

### Model Comparison

_Add screenshot here_

### Churn Prediction

_Add screenshot here_

---

# 🔮 Future Improvements

- Add prediction probability.
- Improve UI with readable categorical options.
- Deploy using Docker.
- Add SHAP explainability for model predictions.
- Integrate a database for storing prediction history.
- Add user authentication.

---

# 👩‍💻 Author

**Rishika Yadav**

**B.Tech – Artificial Intelligence & Machine Learning**

LNCT Bhopal

GitHub: https://github.com/YOUR_USERNAME

LinkedIn: https://www.linkedin.com/in/YOUR_LINKEDIN

---

# 📄 License

This project is developed for educational and learning purposes.

---

## ⭐ If you found this project helpful, don't forget to star the repository!
