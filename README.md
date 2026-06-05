# 🏠 House Price Prediction System

A Machine Learning web application that predicts house prices based on various property features using a **Gradient Boosting Regressor** model. The application is built with **Python, Flask, Scikit-learn, Pandas, and Bootstrap**.

---

## 📌 Project Overview

This project uses the Ames Housing Dataset to predict house prices based on important numerical and categorical features.

The workflow includes:

* Data preprocessing
* Feature selection
* One-Hot Encoding for categorical variables
* Model training and evaluation
* Model serialization using Joblib
* REST API development using Flask
* Interactive Bootstrap-based web interface

---

## 🚀 Features

* Predict house prices instantly
* User-friendly Bootstrap UI
* Flask REST API endpoint
* Gradient Boosting Regression model
* Automatic handling of categorical features
* Responsive design

---

## 🛠 Technologies Used

### Programming Language

* Python 3.x

### Libraries

* Pandas
* NumPy
* Scikit-learn
* Joblib
* Flask

### Frontend

* HTML5
* CSS3
* Bootstrap 5
* JavaScript

---

## 📊 Dataset Features

The model uses the following features:

### Numerical Features

* OverallQual
* GrLivArea
* GarageCars
* GarageArea
* TotalBsmtSF
* 1stFlrSF
* FullBath
* TotRmsAbvGrd
* YearBuilt
* YearRemodAdd

### Categorical Features

* MSZoning
* Utilities
* BldgType
* Heating
* KitchenQual
* SaleCondition
* LandSlope

---

## 🤖 Machine Learning Model

### Model Used

GradientBoostingRegressor

### Why Gradient Boosting?

* High prediction accuracy
* Handles non-linear relationships effectively
* Reduces overfitting compared to individual decision trees
* Performs well on structured tabular datasets

---

## 📂 Project Structure

```text
house-price-prediction/
│
├── app.py
├── best_model.pkl
├── model_columns.pkl
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── notebooks/
│   └── HousePricePrediction.ipynb
│
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/house-price-prediction.git

cd house-price-prediction
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## 📡 API Endpoint

### Predict House Price

**Endpoint**

```http
POST /predict
```

### Sample Request

```json
{
    "OverallQual": 7,
    "GrLivArea": 1710,
    "GarageCars": 2,
    "GarageArea": 548,
    "TotalBsmtSF": 856,
    "1stFlrSF": 856,
    "FullBath": 2,
    "TotRmsAbvGrd": 8,
    "YearBuilt": 2003,
    "YearRemodAdd": 2003,
    "MSZoning": "RL",
    "Utilities": "AllPub",
    "BldgType": "1Fam",
    "Heating": "GasA",
    "KitchenQual": "Gd",
    "SaleCondition": "Normal",
    "LandSlope": "Gtl"
}
```

### Sample Response

```json
{
    "predicted_price": 303245.37
}
```

---

## 📈 Model Workflow

1. Load dataset
2. Handle missing values
3. Select important numerical and categorical features
4. Apply One-Hot Encoding using `pd.get_dummies()`
5. Split data into training and testing sets
6. Train multiple regression models
7. Evaluate models using:

   * MAE
   * MSE
   * RMSE
   * R² Score
8. Select the best-performing model
9. Save model using Joblib
10. Deploy with Flask

---

## 📷 Application Screenshot

Add screenshots of:

* Home Page
* Prediction Result Page

Example:

```text
screenshots/home.png
screenshots/result.png
```

---

## 🎯 Future Improvements

* Deploy to Render or Railway
* Add model comparison dashboard
* Improve UI/UX
* Add data visualization charts
* Implement user authentication
* Containerize using Docker

---

## 👨‍💻 Author

Mohammed Naseef S

Machine Learning & Python Developer

---

## 📄 License

This project is licensed under the MIT License.
