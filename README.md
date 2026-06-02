# Tracking-Maternal-Health-Progress


## 📖 Project Overview

This project analyzes maternal health data to support **Sustainable Development Goal (SDG) 3.1**, which aims to reduce maternal mortality.
It uses machine learning to predict **Maternal Mortality Ratio (MMR)** based on health indicators.

---

## 🎯 Objective

* Predict maternal mortality trends
* Analyze impact of healthcare factors
* Provide data-driven insights for improvement

---

## 📊 Dataset

* Source: **Data.gov.in (SDG National Indicator Framework)**
* Features used:

  * Year (TimePeriod)
  * Antenatal Care (%)
  * Skilled Birth Attendance (%)
  * Adolescent Birth Rate
  * Healthcare Expenditure
* Target:

  * Maternal Mortality Ratio (DataValue)

---

## 🤖 Machine Learning Models

* Decision Tree Classifier (initial model)
* Linear Regression (final model for prediction)

---

## ☁️ Technologies Used

* IBM Watson Studio
* IBM Cloud Object Storage
* IBM Machine Learning (Deployment)
* Python (Pandas, Scikit-learn)
* Django (Web Application)

---

## ⚙️ Workflow

1. Data Collection from Data.gov.in
2. Data Cleaning & Preprocessing
3. Model Training (Regression)
4. Model Deployment on IBM Cloud
5. Web Interface for Prediction

---

## 🚀 Features

* User input for health indicators
* Real-time prediction using deployed model
* Simple web interface

---

## 📌 How to Run

1. Clone the repository
2. Install dependencies (`pip install django requests`)
3. Run server:

   ```bash
   python manage.py runserver
   ```
4. Open browser:

   ```
   http://127.0.0.1:8000/
   ```

---

## 📈 Output

* Predicts **Maternal Mortality Ratio (MMR)** based on inputs

---

## 🔮 Future Enhancements

* Add more health indicators
* Improve model accuracy using advanced algorithms
* Interactive dashboards

---

## 👩‍💻 Author

*A.V.SHASHI PREETHI


