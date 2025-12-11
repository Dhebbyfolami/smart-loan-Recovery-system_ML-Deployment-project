# smart-loan-Recovery-system_ML-Deployment-project
This project builds and deploys a *machine learning-powered loan recovery prediction system*.  
It predicts the likelihood that a borrower will repay their loan and flags high‑risk borrowers to assist financial institutions in effective loan recovery.

The system includes:
- Data preprocessing & feature engineering  
- Multiple ML models (Logistic Regression, Decision Tree, Random Forest, SVM)  
- Model evaluation using standard metrics  
- Saving best-performing model  
- Deployment using *FastAPI* for real-time inference  

---

## 🚀 Features
- Predicts repayment probability
- Identifies high-risk borrowers
- Scalable API for integration with applications
- End-to-end ML pipeline: preprocessing → training → evaluation → deployment

---

## 📁 Project Structure

├── data/
│   └── Smart Loan Recovery System.csv
├── model/
│   └── loan_model.pkl
├── api/
│   └── main.py  # FastAPI deployment script
├── notebooks/
│   └── Model_Deployment_ML_project2.ipynb
├── requirements.txt
└── README.md


---

## 🧠 Machine Learning Workflow

### 1. Data Preprocessing
- Missing value handling  
- Numeric column extraction  
- Scaling using StandardScaler  
- Target mapping:
  - Fully Recovered → 1  
  - Partially Recovered → 1  
  - Written Off → 0  

### 2. Feature Engineering
Examples:
- Debt-to-income ratio
- Additional engineered features based on dataset fields

### 3. Model Training
Trained models include:
- Logistic Regression  
- Decision Tree  
- Random Forest (best model)  
- Support Vector Machine  

Evaluation metrics:
- Accuracy  
- Precision  
- Recall  
- F1-score  
- ROC-AUC  

### 4. Deployment
The trained loan_model.pkl is served through a *FastAPI* application.

Endpoints:

GET  /
POST /predict


Example prediction request:
json
{
  "Loan_Amount": 25000,
  "Monthly_Income": 5000,
  "Interest_Rate": 12.5,
  "Loan_Term": 24
}


---

## 🛠 Installation


pip install -r requirements.txt


Run API server:

uvicorn main:app --reload


---

## 📦 Inference Logic
- Inputs transformed into numerical feature vectors  
- Model predicts repayment probability  
- Borrowers flagged as *high risk* when probability < 0.5  

---

## 📑 Model Card
See MODEL_CARD.md for detailed documentation on model assumptions, limitations, and ethical considerations.

---

💬 Contact

Your Name
📧 Email: dhebbyfolasayomi97@gmail.com
🔗 GitHub: https://github.com/Debbyfolami
💼 LinkedIn: [(Oluwasayo Adeola)](https://www.linkedin.com/in/oluwasayo-adeola-a035472a2?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)


---

📝 License

This project is licensed under the MIT License.

---
