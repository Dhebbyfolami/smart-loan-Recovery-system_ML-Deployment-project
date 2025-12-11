# Project Structure

Recommended repository layout:


.
├── api/
│   └── main.py              # FastAPI app
├── data/
│   └── Smart Loan Recovery System.csv
├── model/
│   └── loan_model.pkl
├── notebooks/
│   └── Model_Deployment_ML_project2.ipynb
├── src/
│   ├── data_processing.py   # preprocessing & feature engineering
│   ├── training.py          # training and evaluation scripts
│   └── inference.py         # helper functions for model inference
├── tests/
│   └── test_pipeline.py
├── Dockerfile
├── requirements.txt
├── README.md
└── MODEL_CARD.md
