import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier

# Load the preprocessed data
X_train = pd.read_csv("Resources/X_train.csv")
y_train = pd.read_csv("Resources/y_train.csv")["isFraud"]

# Select two basic features
selected_features = ['TransactionDT', 'TransactionAmt']
X_train_selected = X_train[selected_features]

# Train the XGBoost model
xgb_model = XGBClassifier(use_label_encoder=False, random_state=42)
xgb_model.fit(X_train_selected, y_train, eval_metric='logloss')

# Streamlit app
st.title("Fraud Detection")

transaction_dt = st.number_input("TransactionDT", min_value=0, value=100000)
transaction_amt = st.number_input("TransactionAmt", min_value=0.0, value=50.0)

if st.button("Predict"):
    input_data = pd.DataFrame({"TransactionDT": [transaction_dt],
                               "TransactionAmt": [transaction_amt]})
    prediction = xgb_model.predict(input_data)
    st.write("Prediction: ", "Fraud" if prediction[0] == 1 else "Not Fraud")