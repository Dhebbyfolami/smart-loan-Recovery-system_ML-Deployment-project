## Overview
This project exposes a FastAPI application that serves model predictions.

## Endpoints

### GET /
Health check.
*Response*
- 200 OK
json
{"message": "Loan Recovery Prediction API is running!"}


### POST /predict
Get repayment probability and high-risk flag.

*Request body (JSON)*
Include required numeric features used by the model. Example:
json
{
  "Loan_Amount": 25000,
  "Monthly_Income": 5000,
  "Interest_Rate": 12.5,
  "Loan_Term": 24
}


*Response*
json
{
  "repayment_probability": 0.72,
  "high_risk_borrower": false
}


*Notes*
- Ensure feature names and data types match training pipeline.
- Missing fields should be handled by the client or validated by the API.
