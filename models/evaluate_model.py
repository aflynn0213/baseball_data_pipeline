import pandas as pd
from sklearn.metrics import classification_report
import joblib

# Load the test data
def load_test_data(file_path):
    return pd.read_csv(file_path)

# Evaluate the model
def evaluate_model(model, test_data):
    X_test = test_data.drop('target', axis=1)
    y_test = test_data['target']
    
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred)
    print(report)

if __name__ == "__main__":
    test_data = load_test_data('data/test_data.csv')  # Path to your test data
    model = joblib.load('models/trained_model.pkl')    # Load the trained model
    evaluate_model(model, test_data)
