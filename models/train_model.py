import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Load the preprocessed data
def load_data(file_path):
    return pd.read_csv(file_path)

# Train the model
def train_model(data):
    X = data.drop('target', axis=1)  # Features
    y = data['target']                # Target variable
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    
    return model

# Save the trained model
def save_model(model, model_path):
    joblib.dump(model, model_path)

if __name__ == "__main__":
    data = load_data('data/processed_data.csv')  # Path to your preprocessed data
    model = train_model(data)
    save_model(model, 'models/trained_model.pkl')  # Save path for the model
