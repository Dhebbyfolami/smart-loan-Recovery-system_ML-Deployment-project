# Installation Guide

## Clone repository
bash
git clone <repo-url>
cd <repo-directory>


## Create virtual environment (recommended)
bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate


## Install dependencies
bash
pip install -r requirements.txt


## Prepare data
Place Smart Loan Recovery System.csv in the data/ directory.

## Train model (example)
Run training script (if available):
bash
python src/training.py --data data/Smart\ Loan\ Recovery\ System.csv


## Run the API
bash
uvicorn api.main:app --reload
