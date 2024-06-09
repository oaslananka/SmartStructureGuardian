
# Setup Guide

This guide will help you set up the Smart Structure Guardian project on your local machine.

## Prerequisites

Make sure you have the following software installed on your system:
- Python 3.6 or higher
- Git

## Steps

### 1. Clone the Repository

First, clone the repository from GitHub to your local machine.

```bash
git clone https://github.com/oaslananka/SmartStructureGuardian.git
cd SmartStructureGuardian
```

### 2. Create and Activate a Virtual Environment (Optional but Recommended)

It's a good practice to use a virtual environment to manage dependencies for your project.

#### On macOS/Linux

```bash
python3 -m venv env
source env/bin/activate
```

#### On Windows

```bash
python -m venv env
env\Scripts\activate
```

### 3. Install the Required Packages

Install the required Python packages using the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 4. Set Up the Project Structure

Ensure the following directories are created if they do not exist:

```bash
mkdir -p data/raw
mkdir -p data/processed
mkdir -p outputs/figures
mkdir -p outputs/reports
mkdir -p models
```

### 5. Run the Project Scripts

Follow these steps to run the project scripts:

1. **Simulate sensor data:**

    ```bash
    python src/data_simulation.py
    ```
    This script generates simulated sensor data and saves it to `data/raw/simulated_sensor_data.csv`.

2. **Preprocess the sensor data:**

    ```bash
    python src/data_preprocessing.py
    ```
    This script preprocesses the sensor data and saves it to `data/processed/preprocessed_sensor_data.csv`.

3. **Train the anomaly detection model:**

    ```bash
    python src/model_training.py
    ```
    This script trains the anomaly detection model and saves it to `models/anomaly_detection_model.pkl`.

4. **Detect anomalies in the sensor data:**

    ```bash
    python src/anomaly_detection.py
    ```
    This script detects anomalies in the sensor data and saves the results to `outputs/reports/anomaly_detection_results.csv`.

5. **Visualize the anomalies:**

    ```bash
    python src/visualization.py
    ```
    This script generates a 3D animated GIF showing the bending and deformation of the bridge and saves it to `outputs/figures/bridge_bending_animation.gif`.

## Additional Information

- Ensure you have sufficient permissions to create directories and files in your working directory.
- If you encounter any issues, check the [README.md](README.md) file for more details or troubleshooting steps.

## Author

This project was created by [oaslananka](https://github.com/oaslananka).
