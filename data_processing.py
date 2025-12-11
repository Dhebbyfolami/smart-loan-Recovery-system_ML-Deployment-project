# data_processing.py

import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df

def preprocess(df: pd.DataFrame):
    # Map target variable
    df['target'] = df['Recovery_Status'].map({
        'Fully Recovered': 1,
        'Partially Recovered': 1,
        'Written Off': 0
    })
    df = df.dropna(subset=['target'])
    df = df.fillna(df.median(numeric_only=True))

    # Feature engineering
    if 'Loan_Amount' in df.columns and 'Monthly_Income' in df.columns:
        df['debt_to_income'] = df['Loan_Amount'] / (df['Monthly_Income'] + 1)

    # Select numeric features
    X = df.select_dtypes(include=['int64', 'float64']).drop(columns=['target'], errors='ignore')
    y = df['target']

    # Scale inputs
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y, scaler, X.columns
