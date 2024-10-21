import os
import logging
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score
from your_model_package import load_model, get_new_data  # Replace with your own module

# Set up logging
logging.basicConfig(filename='logs/model_monitor.log', level=logging.INFO)

# Load your model
model = load_model('path_to_your_saved_model.pkl')

# Thresholds for monitoring (customize these as needed)
ACCURACY_THRESHOLD = 0.9
DRIFT_THRESHOLD = 0.05  # e.g., for statistical test

def monitor_model():
    # Step 1: Get new production data
    X_new, y_true = get_new_data()  # Function to get new data and true labels
    
    # Step 2: Make predictions
    y_pred = model.predict(X_new)
    
    # Step 3: Evaluate performance
    accuracy = accuracy_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred, average='macro')
    
    logging.info(f"Current accuracy: {accuracy}")
    logging.info(f"Current F1 Score: {f1}")
    
    # Step 4: Check for drift
    check_for_drift(X_new, y_pred)
    
    # Step 5: Performance alerting
    if accuracy < ACCURACY_THRESHOLD:
        logging.error(f"Model accuracy dropped below threshold! Accuracy: {accuracy}")
        alert_team(f"Model accuracy dropped to {accuracy}. Needs investigation.")
    
    # Step 6: Resource usage (optional)
    check_resource_usage()

def check_for_drift(new_data, predictions):
    # Compare new data distribution with training data
    # For simplicity, let's assume we're checking the mean and std of features
    training_mean = np.load('training_feature_mean.npy')  # Pre-saved stats from training data
    training_std = np.load('training_feature_std.npy')
    
    new_data_mean = np.mean(new_data, axis=0)
    new_data_std = np.std(new_data, axis=0)
    
    drift_detected = np.any(np.abs(new_data_mean - training_mean) > DRIFT_THRESHOLD)
    if drift_detected:
        logging.warning("Data drift detected! Check model inputs.")
        alert_team("Data drift detected! Model performance might be impacted.")
    
def check_resource_usage():
    # This function could use libraries like `psutil` to monitor CPU and memory usage
    import psutil
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    
    logging.info(f"CPU usage: {cpu_usage}%")
    logging.info(f"Memory usage: {memory_usage}%")
    
    if cpu_usage > 80:
        logging.warning(f"High CPU usage detected: {cpu_usage}%")
    
    if memory_usage > 80:
        logging.warning(f"High memory usage detected: {memory_usage}%")

def alert_team(message):
    # Send alerts (you can integrate with email, Slack, etc.)
    print(f"ALERT: {message}")  # For simplicity, we're just printing

if __name__ == "__main__":
    monitor_model()
