# Project_4 Fraud Detection System For Online Transaction (Using Machine Learning)

#### <p align="center">
  <img src="https://user-images.githubusercontent.com/112173540/225614794-ed8645e6-c6b5-4cea-bfd3-c70c8596f44e.jpg"/>

## Applying RandomForest and XGBoost for Fraud Detection and Developed with Streamlit  
This project aims to build a fraud detection system using machine learning techniques to classify transactions as fraudulent or non-fraudulent. The dataset is derived from the IEEE-CIS Fraud Detection Kaggle competition, and various preprocessing steps are performed to ensure optimal model performance. The project compares multiple machine learning models and selects the best one based on performance metrics.

## Table of Contents
- Introduction  
- Data Acquisition and Exploration  
- Data Preprocessing  
- Model Selection and Evaluation  
**Model Performance Metrics**  
**Hyperparameter Tuning**  
- Model Development with Streamlit  
- Key Takeaways  
- Challenges Faced  
- Repository Contents
- GooGLE-Drive-Data-Folder


## Introduction

This project aims to tackle the challenge of online transaction fraud detection and emphasize the significance of timely and accurate fraud identification. The goal is to create a machine learning model to assess the probability of fraudulent transactions (classification problem).

## Data Acquisition and Exploration

The dataset is sourced from [IEEE-CIS Fraud Detection competition](https://www.kaggle.com/c/ieee-fraud-detection/overview) Kaggle competition. It consists of transactional and identity data, with various features and a binary target variable (isFraud).

The data is broken into two files **`identity.csv`** and **`transaction.csv`**, each having separate files for train and test data which are merged on the `TransactionID` column. Not all transactions have corresponding identity information. The identity data includes information about the user, such as device type, browser, and IP address. The transaction data contains details about each transaction, including the transaction amount, product code, and card information.

#### The datasets are too large to load into Github. 
- To run our code, the dataset can be downloaded from here [IEEE-CIS Fraud Detection competition](https://www.kaggle.com/c/ieee-fraud-detection/overview).

**The libraries used are**:  
- numpy
- pandas
- matplotlib
- seaborn
- sklearn


## Data Preprocessing   

**To prepare the data for modeling, several preprocessing steps are performed:**

**Loading the data**  
- The identity and transaction data are loaded from CSV files using pandas.  
  
**Merging the datasets**  
- The identity and transaction datasets are merged on the TransactionID column using a left join to ensure that all transaction data is retained.  
  
**Handling missing values:**  
- Columns with more than 40% missing values are dropped from the dataset. For the remaining columns, missing values are imputed with the mean of each column.  
  
**Handling infinity values**
- Infinity values are replaced with NaN.  
  
**Filling NaN values:**  
- NaN values are filled with the mean of each column.  
  
**Storing cleaned data:**
- The cleaned data is saved to CSV file.  
  
**Label Encoding**
- Encode categorical variables with LabelEncoder by Convert string, category, object type variables to integers type.  
  
**Feature Scaling**  
- Feature scaling is performed to normalise the data using the StandardScaler from scikit-learn. This step ensures that all features have the same scale, which helps improve the performance of machine learning models, particularly those sensitive to feature scales, such as gradient-based methods.  
  
 **SQL database**  
 - Store processed data in an SQL database for easier access and retrieval during model training and evaluation. 

## Model Selection and Evaluation
The project explores various machine learning models, including:

  - Decision Tree
  - AdaBoost
  - Random Forest
  - XGBoost
The models are trained on a portion of the training data and validated on the remaining data. Model performance is compared using ROC AUC scores and classification report.The XGBoost classifier demonstrates the best performance, making it the ideal choice for this dataset.  

**Model Performance Metrics**  
The models' performance is compared using ROC AUC scores and classification reports.**  

**Hyperparameter Tuning**  
GridSearchCV is attempted for RandomForest and XGBoost classifiers. However, due to computational limitations, the tuning process could not be completed. The XGBoost classifier with built-in regularization techniques (L1, L2, and max depth constraints) is used for real-time fraud detection with Streamlit.**  

## Model Development with Streamlit 
In addition to the Jupyter Notebook implementation, the project can be deployed using Streamlit, a popular framework for building data-driven web applications. The Streamlit application can interactively display the performance metrics of different models and show the predictions made by the best-performing model.

To deploy the project with Streamlit, follow these steps:

  - **Install Streamlit using the following command:**
      -  pip install streamlit
      
  - Create a new Python script named `app.py` and adapt the existing code to work with Streamlit. 
  - Use Streamlit commands to load the data, train the models, and display the performance metrics and predictions.

  - **Run the Streamlit application using the following command:**
      - streamlit run app.py

  -  **Open the web application in the browser using the URL provided by Streamlit.**  
  We can interact with the application to explore the dataset, model performance metrics, and predictions made by the best-performing model (XGBoost in this case).

## Key Takeaways
- Request more instances of fraudulent transactions from the organization to improve model training and prediction accuracy.  
- Address imbalanced dataset challenges with techniques such as oversampling, undersampling, or using cost-sensitive learning.    
- Optimize computational resources and training times by leveraging scalable solutions like Apache Spark or distributed computing.
- Seek clarity on column names to potentially merge related variables, inform feature engineering, and improve model interpretability.  
## Challenges Faced
- Sparsity of the dataset
- A large number of missing values
- Imbalanced 'isFraud' variable
- Dataset size and complexity made hyperparameter tuning

## Repository Contents
  
The repository is organized into the following directories and files:  
  
**README.md:**
  - This file, containing an overview of the project, instructions, and a description of the repository contents.  
  
**code:** 
  - Folder containing the Jupyter notebooks, Python scripts, and Streamlit app code.  
  
**Final Notebooks:**  
  - Folder containing the final versions of the Jupyter notebooks used in the project.  
  
**Test notebooks:**  
  - Folder containing the test notebooks used during the project development.  
  
**Streamlit App code:**  
  - Folder containing the Streamlit app code for deploying the XGBoost classifier.  
  
**Presentations Slides **  
  - Predicting Fraudulent Online Transactions.pdf: PDF file containing the presentation slides.  
  
**Images: **  
  - Folder containing images used in the project.  
  
**SQL files:**  
  -Folder containing SQL files related to the project.  
  
**.ipynb_checkpoints:**  
  - Folder containing Jupyter notebook checkpoints.  
  
**clean_data_code_processed.csv.ipynb:**  
  - Jupyter notebook for processing the cleaned data.  
  
**cleaned_data_script.h5.ipynb:**  
  - Jupyter notebook containing the cleaned data script.  

## Google-Drive-Data-Folder"
- Due to the large size of the dataset (1.35GB), it is not included in the GitHub repository. You can access the original data files and all other project files in this [Google Drive folder](bit.ly/3z8kZaJ).


