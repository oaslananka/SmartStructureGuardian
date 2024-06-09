# anomaly_detection.py
# This script uses the trained model to detect anomalies in new sensor data.
# Author: Osman ASLAN Github: @oaslananka

import pandas as pd
import joblib


def detect_anomalies(data, model_path):
    """
    Detects anomalies in the sensor data using the trained model.

    Parameters:
        data (pd.DataFrame): The preprocessed sensor data.
        model_path (str): Path to the trained model.

    Returns:
        pd.DataFrame: A DataFrame containing the sensor data with anomaly labels.
    """
    # Load the trained model
    model = joblib.load(model_path)

    # Predict anomalies
    data['anomaly'] = model.predict(data[['vibration', 'stress', 'temperature']])

    return data


if __name__ == "__main__":
    # File path to the preprocessed sensor data
    file_path = 'data/processed/preprocessed_sensor_data.csv'

    # Load the preprocessed data
    preprocessed_data = pd.read_csv(file_path)

    # Path to the trained model
    model_path = 'models/anomaly_detection_model.pkl'

    # Detect anomalies
    anomaly_data = detect_anomalies(preprocessed_data, model_path)

    # Save the data with anomaly labels to a CSV file
    anomaly_data.to_csv('outputs/reports/anomaly_detection_results.csv', index=False)

    print("Anomaly detection results saved to 'outputs/reports/anomaly_detection_results.csv'")
