# training.py

import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from data_processing import load_data, preprocess

def train_model(data_path: str, model_path: str = "model/loan_model.pkl"):
    df = load_data(data_path)
    X, y, scaler, feature_names = preprocess(df)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:,1]

    metrics = {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred),
        "recall": recall_score(y_test, y_pred),
        "f1": f1_score(y_test, y_pred),
        "roc_auc": roc_auc_score(y_test, y_proba)
    }

    # Save model artifacts
    joblib.dump({
        "model": model,
        "scaler": scaler,
        "features": list(feature_names)
    }, model_path)

    return metrics

if _name_ == "_main_":
    print(train_model("data/Smart Loan Recovery System.csv"))
