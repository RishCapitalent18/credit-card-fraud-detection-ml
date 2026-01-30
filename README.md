# 🛡️ End-to-End Credit Card Fraud Detection System  
### Neural Networks & Anomaly Detection

## Overview
This project implements a **production-oriented credit card fraud detection system** that identifies anomalous and fraudulent transactions using **neural networks combined with unsupervised anomaly detection**.  
The system follows a complete **data → model → evaluation → deployment** workflow, emphasizing **scalability, interpretability, and real-world applicability**.

---

## Problem Statement
Credit card fraud detection requires **high accuracy under extreme class imbalance**, low latency, and the ability to **generalize to evolving fraud patterns**.  
Traditional rule-based approaches fail to scale and adapt, motivating a **data-driven machine learning system** that combines **unsupervised anomaly discovery** with **supervised classification**.

---

## System Architecture
**Transactional Data → Feature Engineering → Anomaly Detection → Fraud Classification → Risk Scoring → Deployment**

### Core Components
1. **Data Processing Pipeline**
   - Transaction normalization and feature consistency checks  
   - Reproducible train/test splits  

2. **Anomaly Detection**
   - **Self-Organizing Maps (SOMs)** used to identify anomalous transaction clusters  

3. **Fraud Classification**
   - Neural-network classifier trained on anomaly-aware features  
   - Probability-based fraud risk scoring for interpretability  

4. **Deployment**
   - Web-based application enabling inference and visualization  

---

## Data
- **Input:** Structured transactional data containing numerical behavioral features  
- **Processing Steps:**
  - Feature scaling and normalization  
  - Dimensional validation and consistency checks  

**Note:** Full datasets are excluded due to privacy and licensing constraints.  
Sample schemas and preprocessing scripts are provided to support reproducibility.

---

## Models & Methods
- **Self-Organizing Maps (SOMs)**
  - Enable unsupervised detection of anomalous spending behavior  
  - Effective under highly imbalanced fraud scenarios  

- **Neural Networks**
  - Supervised classification layered on top of anomaly signals  
  - Iterative epoch tuning to optimize convergence and generalization  

- **Risk Scoring**
  - Probabilistic outputs generated to support downstream decision-making  

---

## Evaluation & Results
- **Detection Accuracy:** **93.19%**  
- **Key Observations:**
  - SOMs improved identification of anomalous transaction patterns  
  - Neural networks refined precision when trained on anomaly-aware features  
  - Probability-based outputs improved interpretability of fraud predictions  

---

## Deployment & Integration
The system is deployed as a **full-stack web application** integrating:

- **Python** for machine learning pipelines  
- **Apache Spark** for scalable data processing  
- **PHP + XAMPP + Apache Server** for backend integration  
- **HTML5** for frontend visualization  

This deployment validates the model in a **realistic inference environment**, beyond offline experimentation.

---

## Tech Stack
- **Languages:** Python, PHP  
- **Machine Learning:** Neural Networks, Self-Organizing Maps (SOMs)  
- **Data Processing:** Apache Spark  
- **Web & Deployment:** Apache Server, XAMPP, HTML5  
- **Development:** Jupyter Notebook  

---

## Key Engineering Learnings
- Combining **unsupervised anomaly detection with supervised learning** improves fraud detection robustness  
- Feature normalization and epoch tuning significantly affect convergence stability  
- Probability-based outputs increase trust and interpretability in ML-driven systems  
- End-to-end deployment surfaces constraints not visible during offline training  

---

## Future Improvements
- Real-time streaming ingestion using **Kafka + Spark Streaming**  
- Model drift detection and monitoring  
- Containerized deployment using **Docker**  
- Distributed inference and fault-tolerant serving  
- Expanded evaluation using **ROC-AUC and Precision–Recall metrics**

---

## How to Run
```bash
# Clone the repository
git clone https://github.com/<your-username>/credit-card-fraud-detection-ml.git
cd credit-card-fraud-detection-ml

# Install dependencies
pip install -r requirements.txt

# Train the model
python src/models/train.py
