"""
Evaluation utilities for the credit card fraud detection model.

Responsibilities:
- Load trained ANN model.
- Compute accuracy on a held-out test set.
- Optionally plot loss/accuracy curves.
"""

def load_model(model_path: str):
    """Load trained TensorFlow/Keras model from disk."""
    raise NotImplementedError

def evaluate(model, X_test, y_test):
    """Return accuracy and other metrics on the test set."""
    raise NotImplementedError

def plot_learning_curves(history, output_dir: str):
    """Plot loss and accuracy vs epochs for documentation."""
    raise NotImplementedError
