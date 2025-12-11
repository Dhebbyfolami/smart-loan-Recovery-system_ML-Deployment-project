# Model Card — Smart Loan Recovery System

## Model Summary
This Random Forest classifier predicts loan repayment likelihood to identify high-risk borrowers.

### Intended Use
- Loan recovery departments
- Risk analysis teams
- Automated decision-support systems

### Training Data
- Dataset: Smart Loan Recovery System.csv  
- Target:
  - 1 = fully/partially recovered  
  - 0 = written off  

### Metrics
- Accuracy  
- Precision  
- Recall  
- F1-score  
- ROC-AUC  

### Ethical Considerations
- Avoid discriminatory inputs  
- Monitor model drift over time  
- Ensure transparency in automated decision-making  

### Limitations
- Model performance depends on dataset quality  
- May not generalize across different financial institutions
