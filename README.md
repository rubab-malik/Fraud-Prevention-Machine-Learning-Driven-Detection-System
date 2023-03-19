# Project_4
Machine Learning

![images](https://user-images.githubusercontent.com/112173540/225614794-ed8645e6-c6b5-4cea-bfd3-c70c8596f44e.jpg)


# IEEE-CIS Fraud Detection
### Can you detect fraud from customer transactions?
### Machine Learning to detect transaction fraud using the IEEE-CIS Fraud Detection

### Introduction

The [IEEE-CIS Fraud Detection competition](https://www.kaggle.com/c/ieee-fraud-detection/overview) was held on Kaggle during 2019. The goal is to identify whether each online transaction is `fraud` or `not fraud` . In this project, we will detect online fraudulent transactions using machine learning techniques.

We decided to explore this dataset and build models to detect online fraud. Our Random Forest model was able to reach a value of `0.995` on the cleaned dataset.

## **Exploratory Data Analysis (EDA)**
- An observation that was immediately apparent is the imbalanced nature of the data. This shows that 'TransactionDT' is a timedelta gap, not a timestamp.
- Dataset has a very high percentage of missing values, especially the V columns.
- Columns not only had a high amount of missing data, but their distributions also were not normally distributed.
- The distribution of target variable **'isFraud'** has `class imbalance` problem where it shows that 96.5% of data contains non-fraud transaction where as only 3.5% are fraud.

## Dataset
The data is broken into two files **identity.csv** and **transaction.csv**, which are joined by TransactionID. Not all transactions have corresponding identity information.

**The libraries used are**:  
- numpy
- pandas
- matplotlib
- seaborn
- sklearn

**Missing Values**
- Around 414 features contain missing values.
- Top features containing missing values.

**Label Encoding**
- Convert string, category, object type variables to integers type.

## **Model** 
- Logistic Regression
- Random Forest
- Decision Tree

## Results
After creating some baseline models we stick with Random Forests as it was giving better perfomance.

**Challenges**:
- Sparsity of the dataset
- A lot Missing Values
- Imbalanced isFraud Variable


#### The datasets are too large to load into Github. 
To run our code, download the data from Data source: https://www.kaggle.com/competitions/ieee-fraud-detection/data

## Fraud Detection Project
This project aims to build a fraud detection system using machine learning techniques to classify transactions as fraudulent or non-fraudulent. The dataset is derived from the IEEE-CIS Fraud Detection Kaggle competition, and various preprocessing steps are performed to ensure optimal model performance. The project compares multiple machine learning models and selects the best one based on performance metrics.

**Table of Contents**
Introduction
Dataset Description
Data Preprocessing
Feature Scaling
Model Training and Evaluation
Dependencies
Running the Project
deployment with streamlit




#### Introduction
Fraud detection is a crucial aspect of modern financial systems, as it ensures the security and integrity of transactions. This project demonstrates the application of machine learning techniques to identify fraudulent transactions using a dataset from the IEEE-CIS Fraud Detection Kaggle competition.

#### Dataset Description
The dataset consists of identity and transaction data, each having separate files for train and test data. The identity data includes information about the user, such as device type, browser, and IP address. The transaction data contains details about each transaction, including the transaction amount, product code, and card information.

The dataset can be downloaded from here.
The [IEEE-CIS Fraud Detection competition](https://www.kaggle.com/c/ieee-fraud-detection/overview).
#### Data Preprocessing
To prepare the data for modeling, several preprocessing steps are performed:

Loading the data: The identity and transaction data are loaded from CSV files using pandas.

Merging the datasets: The identity and transaction datasets are merged on the "TransactionID" column using a left join to ensure that all transaction data is retained.

Handling missing values: Columns with more than 40% missing values are dropped from the dataset. For the remaining columns, missing values are imputed with the mean of each column.

Handling infinity values: Infinity values are replaced with NaN.

Filling NaN values: NaN values are filled with the mean of each column.

Storing cleaned data: The cleaned data is saved to an SQLite database for easier access and retrieval during model training and evaluation.

#### Feature Scaling
Feature scaling is performed to normalize the data using the StandardScaler from scikit-learn. This step ensures that all features have the same scale, which helps improve the performance of machine learning models, particularly those sensitive to feature scales, such as gradient-based methods.

####  Model Training and Evaluation
Several machine learning models are trained and evaluated on the preprocessed data, including:


Decision Tree
AdaBoost
Random Forest
XGBoost
The models are trained on a portion of the training data and validated on the remaining data. Model performance is compared using ROC AUC scores and accuracy scores. The XGBoost classifier demonstrates the best performance, making it the ideal choice for this dataset.

#### Streamlit Deployment
In addition to the Jupyter Notebook implementation, the project can be deployed using Streamlit, a popular framework for building data-driven web applications. The Streamlit application can interactively display the performance metrics of different models and show the predictions made by the best-performing model.

To deploy the project with Streamlit, follow these steps:

Install Streamlit using the following command:

pip install streamlit
Create a new Python script named app.py and adapt the existing code to work with Streamlit. Use Streamlit commands to load the data, train the models, and display the performance metrics and predictions.

Run the Streamlit application using the following command:

streamlit run app.py
Open the web application in the browser using the URL provided by Streamlit. We can interact with the application to explore the dataset, model performance metrics, and predictions made by the best-performing model (XGBoost in this case).
By deploying this project with Streamlit, We create an interactive web application that allows users to explore the data and understand the performance of various models more effectively. 
