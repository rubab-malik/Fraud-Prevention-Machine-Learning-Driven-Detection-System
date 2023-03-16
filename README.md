# Project_4
Machine Learning

# IEEE-CIS Fraud Detection
### Can you detect fraud from customer transactions?
### Machine Learning to detect transaction fraud using the IEEE-CIS Fraud Detection

### Introduction

The [IEEE-CIS Fraud Detection competition](https://www.kaggle.com/c/ieee-fraud-detection/overview) was held on Kaggle during 2019. The goal is to identify whether each online transaction is `fraud` or `not fraud` . In this project, we will detect online fraudulent transactions using machine learning techniques.

We decided to explore this dataset and build models to detect online fraud. Our Random Forest model was able to reach a value of `0.995` on the cleaned dataset.

## **Exploratoy Data Analysis (EDA)**
- An observation that was immediately apparent is the imbalanced nature of the data. This shows that 'TransactionDT' is a timedelta gap, not a timestamp.
- Dataset has a very high percentage of missing values, especially the V columns.
- Columns not only had a high amount of missing data, but their distributions also were not normally distributed.
- The distribution of target variable **'isFraud'** has `class imbalance` problem where it shows that 96.5% of data contains non-fraud transaction where as only 3.5% are fraud.

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



Data source: https://www.kaggle.com/competitions/ieee-fraud-detection/data
