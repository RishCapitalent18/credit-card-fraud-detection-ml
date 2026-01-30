"""
Train pipeline for credit card fraud detection.

Pipeline:
1. Load credit card transaction / application dataset from CSV.
2. Normalize features (MinMaxScaler).
3. Train Self-Organizing Map (SOM) to highlight anomalous customers.
4. Label potential frauds based on SOM winners.
5. Train a TensorFlow/Keras ANN on labeled data.
6. Save model and export fraud probabilities to CSV for the web app.
"""

def load_data(csv_path: str):
    """Load and return raw dataset from CSV."""
    raise NotImplementedError

def train_som(X):
    """Train SOM on normalized features and return trained SOM + outlier indices."""
    raise NotImplementedError

def train_ann(X, y):
    """Define and train ANN (Keras/TensorFlow) for fraud classification."""
    raise NotImplementedError

def export_probabilities(model, X, output_path: str):
    """Run model inference and write probabilities to a CSV file."""
    raise NotImplementedError

if __name__ == "__main__":
    # TODO: wire the above functions together into the full training pipeline.
    pass
