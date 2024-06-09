# model_training.py
# This script trains a machine learning model to detect anomalies in the sensor data.
# Author: Osman ASLAN Github: @oaslananka

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import IsolationForest
import joblib


def train_anomaly_detection_model(data, model_path):
    """
    Trains an Isolation Forest model for anomaly detection.

    Parameters:
        data (pd.DataFrame): The preprocessed sensor data.
        model_path (str): Path to save the trained model.

    Returns:
        IsolationForest: The trained Isolation Forest model.
    """
    # Split the data into training and test sets
    X_train, X_test = train_test_split(data[['vibration', 'stress', 'temperature']], test_size=0.2, random_state=42)

    # Initialize and train the Isolation Forest model
    model = IsolationForest(contamination=0.05, random_state=42)
    model.fit(X_train)

    # Save the trained model
    joblib.dump(model, model_path)

    return model


if __name__ == "__main__":
    # File path to the preprocessed sensor data
    file_path = 'data/processed/preprocessed_sensor_data.csv'

    # Load the preprocessed data
    preprocessed_data = pd.read_csv(file_path)

    # Path to save the trained model
    model_path = 'models/anomaly_detection_model.pkl'

    # Train the anomaly detection model
    model = train_anomaly_detection_model(preprocessed_data, model_path)

    print(f"Anomaly detection model trained and saved to '{model_path}'")
