📊 Customer Churn Prediction System

Customer Churn Prediction System is an end-to-end Machine Learning web application built using Python and Streamlit that predicts whether a telecom customer is likely to churn. The application helps businesses identify customers at risk of leaving and enables proactive retention strategies through data-driven insights.

The prediction engine uses a Random Forest Classifier trained on the IBM Telco Customer Churn Dataset, providing reliable churn predictions based on customer demographics, subscribed services, contract information, and billing details.

🚀 Features
🔮 Customer Churn Predictor

Enter customer information and instantly predict whether the customer is likely to Stay or Churn.

📊 Dataset Overview

Explore dataset dimensions, preview records, and view statistical summaries.

📈 Exploratory Data Analysis (EDA)

Visualize customer churn distribution and understand the dataset through graphical analysis.

📉 PCA Visualization

View Principal Component Analysis (PCA) visualization to better understand feature distribution and variance.

🏆 Model Comparison

Compare the performance of multiple Machine Learning algorithms including:

Logistic Regression
Decision Tree
Random Forest
K-Nearest Neighbors (KNN)
💡 Business Insights

Receive business recommendations based on churn analysis, helping organizations improve customer retention.

🛠 Tech Stack
Layer	Technology
Programming Language	Python
Machine Learning	Scikit-learn
Data Processing	Pandas, NumPy
Visualization	Matplotlib, Seaborn
Web Framework	Streamlit
Model Storage	Pickle
Version Control	Git & GitHub
🤖 Machine Learning Model

Algorithm

Random Forest Classifier

Dataset

IBM Telco Customer Churn Dataset

Model Accuracy

Model	Accuracy
Logistic Regression	75.94%
Decision Tree	73.31%
Random Forest	78.28%
KNN	69.27%

The Random Forest model achieved the highest accuracy and was selected for deployment.

📌 Features Used (19 Total)
Gender
Senior Citizen
Partner
Dependents
Tenure
Phone Service
Multiple Lines
Internet Service
Online Security
Online Backup
Device Protection
Tech Support
Streaming TV
Streaming Movies
Contract
Paperless Billing
Payment Method
Monthly Charges
Total Charges
📂 Project Structure
customer-churn-prediction/
│
├── data/
│   ├── WA_Fn-UseC_-Telco-Customer-Churn.csv
│   └── README.md
│
├── models/
│   ├── random_forest_model.pkl
│   ├── scaler.pkl
│   └── README.md
│
├── notebooks/
│   ├── Customer_Churn_Prediction.ipynb
│   └── README.md
│
├── streamlit_app/
│   ├── app.py
│   ├── feature_importance.png
│   ├── pca_visualization.png
│   ├── README.md
│   └── pages/
│       ├── 1_Dataset_Overview.py
│       ├── 2_EDA_Dashboard.py
│       ├── 3_Model_Comparison.py
│       ├── 4_Churn_Prediction.py
│       └── 5_Business_Insights.py
│
├── requirements.txt
└── README.md
⚙️ Installation & Setup
Prerequisites
Python 3.10+
Git
Clone Repository
git clone https://github.com/RishikaYadav05/customer-churn-prediction.git

cd customer-churn-prediction
Install Dependencies
pip install -r requirements.txt
Run the Streamlit Application
cd streamlit_app

streamlit run app.py
Open in Browser
http://localhost:8501
📊 Dataset

The project uses the IBM Telco Customer Churn Dataset, which contains customer demographic, service, and billing information.

Dataset includes:

7,043 Customer Records
20 Features
Target Variable:
Churn
Yes = Customer Left
No = Customer Stayed
📈 Exploratory Data Analysis

The application includes:

Customer Churn Distribution
PCA Visualization
Statistical Summary
Dataset Preview
📌 Business Insights

The model suggests several customer retention strategies:

Focus on customers with low tenure.
Encourage customers to switch to long-term contracts.
Monitor customers with high monthly charges.
Reward loyal customers with retention offers.
Create personalized campaigns for customers with high churn risk.
🌐 Deployment

The application is deployed using Streamlit Community Cloud.

Deployment Steps:

Push the project to GitHub.
Connect the repository to Streamlit Community Cloud.
Select:
Main File:
streamlit_app/app.py
Deploy the application.
📦 Requirements

Main libraries used:

streamlit
pandas
numpy
matplotlib
seaborn
scikit-learn
pickle
👩‍💻 Author

Rishika Yadav

B.Tech – Artificial Intelligence & Machine Learning

LNCT Bhopal

GitHub:
https://github.com/RishikaYadav05

📄 License

This project is developed for educational and learning purposes.
