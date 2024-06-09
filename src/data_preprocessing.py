# data_preprocessing.py
# This script preprocesses the simulated sensor data for further analysis.
# Author: Osman ASLAN Github: @oaslananka

import pandas as pd
from sklearn.preprocessing import StandardScaler


def preprocess_data(file_path):
    """
    Preprocesses sensor data by filling missing values and normalizing the data.

    Parameters:
        file_path (str): Path to the CSV file containing the sensor data.

    Returns:
        pd.DataFrame: A DataFrame containing the preprocessed sensor data.
    """
    # Load the sensor data
    df = pd.read_csv(file_path)

    # Fill missing values with the mean of each column
    df.fillna(df.mean(), inplace=True)

    # Normalize the data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df[['vibration', 'stress', 'temperature']])

    # Convert the normalized data back to a DataFrame
    normalized_df = pd.DataFrame(scaled_data, columns=['vibration', 'stress', 'temperature'])

    # Add the sensor_id and position columns back to the DataFrame
    normalized_df['sensor_id'] = df['sensor_id']
    normalized_df['position_x'] = df['position_x']
    normalized_df['position_y'] = df['position_y']

    return normalized_df


if __name__ == "__main__":
    # File path to the simulated sensor data
    file_path = 'data/raw/simulated_sensor_data.csv'

    # Preprocess the data
    preprocessed_data = preprocess_data(file_path)

    # Save the preprocessed data to a CSV file
    preprocessed_data.to_csv('data/processed/preprocessed_sensor_data.csv', index=False)

    print("Preprocessed sensor data saved to 'data/processed/preprocessed_sensor_data.csv'")
