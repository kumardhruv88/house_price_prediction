# 🏠 House Price Prediction – Machine Learning Project

A complete end-to-end **House Price Prediction** system built using Machine Learning.  
This project covers the full ML lifecycle — from **data analysis and model training** to **deployment with a web interface**.

The goal of this project is to strengthen practical understanding of **regression models**, **feature engineering**, **model deployment**, and **ML pipelines**.
deployed on *(https://house-price-prediction-4v1q.onrender.com/=house prediction)*

---

## 📌 Project Overview

- Dataset: Beginner-level House Price dataset from **Kaggle**
- Total Records: **~1000 data points**
- Task: Predict house prices based on multiple numerical and categorical features
- Model Used: **Random Forest Regressor**
- Final R² Score: **~96%**
- Deployment: **Render**
- Frontend: **HTML, CSS**
- Backend: **Flask (Python)**

---

## 📊 Dataset & Exploratory Data Analysis (EDA)

- Performed **column-wise Exploratory Data Analysis**
- Analyzed:
  - Distribution of numerical features
  - Feature relationships with target variable
  - Outliers and skewness
  - Correlation between features
- Insights from EDA guided:
  - Feature selection
  - Model choice
  - Data preprocessing steps

EDA was performed entirely in **Jupyter Notebook**.

---

## 🧠 Machine Learning Approach

### Model Selection
- Used **Random Forest Regressor** due to:
  - Ability to capture non-linear relationships
  - Robustness against overfitting
  - Strong performance on tabular data

### Preprocessing
- Applied **StandardScaler** for feature scaling
- Built a **Pipeline** to ensure:
  - Consistent preprocessing during training and inference
  - Clean and production-ready workflow

### Hyperparameter Tuning
- Tuned key Random Forest parameters such as:
  - `n_estimators`
  - `max_depth`
  - `min_samples_split`
  - `min_samples_leaf`
- Achieved optimal performance with **~96% R² score**

---

## ⚙️ Model Persistence

- Trained model saved as a **`.pkl` file**
- Model loaded during inference for prediction
- Ensures fast and consistent predictions without retraining

---

## 🌐 Web Application & Deployment

### Backend
- Built using **Flask**
- Handles:
  - User input validation
  - Feature preprocessing
  - Model inference
  - Price prediction response

### Frontend
- Simple and clean UI built with **HTML & CSS**
- User-friendly input form for:
  - House features
  - Real-time prediction display

### Deployment
- Deployed on **Render**
- Fully functional end-to-end ML web application

---

## 🛠️ Tech Stack

- **Python**
- **Pandas, NumPy**
- **Scikit-learn**
- **Matplotlib / Seaborn (EDA)**
- **Flask**
- **HTML, CSS**
- **Pickle (.pkl)**
- **Render**
- **Git & GitHub**

---


---

## 🎯 Key Learnings

- End-to-end ML project workflow
- Practical understanding of **Random Forest working**
- Importance of **feature scaling**
- Hyperparameter tuning for performance optimization
- Building and using **ML pipelines**
- Model serialization and deployment
- Connecting ML models with web applications

---

## 🚀 Future Improvements

- Add more advanced feature engineering
- Try Gradient Boosting / XGBoost
- Improve UI/UX
- Add logging and error handling
- Deploy with Docker

---


## ⭐ Acknowledgements

- Kaggle for the dataset
- Open-source ML community

---

⭐ If you find this project useful, feel free to star the repository!

