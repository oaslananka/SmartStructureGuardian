# data_simulation.py
# This script simulates sensor data for a bridge structure.
# Author: Osman ASLAN Github: @oaslananka

import numpy as np
import pandas as pd


def generate_sensor_data(num_sensors, num_samples):
    """
    Generates simulated sensor data for a given number of sensors and samples.

    Parameters:
        num_sensors (int): Number of sensors.
        num_samples (int): Number of samples for each sensor.

    Returns:
        pd.DataFrame: A DataFrame containing the simulated sensor data.
    """
    data = {
        'sensor_id': [],
        'position_x': [],
        'position_y': [],
        'vibration': [],
        'stress': [],
        'temperature': []
    }

    # Sensor positions (for demonstration purposes, we place them linearly along the bridge)
    sensor_positions = np.linspace(0, 100, num_sensors)

    for i in range(num_sensors):
        for _ in range(num_samples):
            data['sensor_id'].append(i + 1)
            data['position_x'].append(sensor_positions[i])
            data['position_y'].append(5)  # Assuming all sensors are at the same width position

            # Simulating sensor data with normal distribution
            data['vibration'].append(np.random.normal(loc=0, scale=0.5))
            data['stress'].append(np.random.normal(loc=0, scale=1.0))
            data['temperature'].append(np.random.normal(loc=25, scale=5))

    return pd.DataFrame(data)


if __name__ == "__main__":
    # Number of sensors and samples
    num_sensors = 10
    num_samples = 100

    # Generate simulated data
    sensor_data = generate_sensor_data(num_sensors, num_samples)

    # Save the simulated data to a CSV file
    sensor_data.to_csv('data/raw/simulated_sensor_data.csv', index=False)

    print("Simulated sensor data generated and saved to '../data/raw/simulated_sensor_data.csv'")
