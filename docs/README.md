
# Smart Structure Guardian

This project simulates sensor data for a bridge structure and uses machine learning to detect anomalies. The project includes data simulation, preprocessing, model training, anomaly detection, and visualization.

## Table of Contents
- [Project Structure](#project-structure)
- [Setup](#setup)
- [Usage](#usage)
- [Visualization](#visualization)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## Project Structure

```
SmartStructureGuardian
│
├── data
│   └── raw
│   └── processed
│
├── notebooks
│   └── data_simulation.ipynb
│   └── data_analysis.ipynb
│   └── anomaly_detection.ipynb
│
├── src
│   ├── data_simulation.py
│   ├── data_preprocessing.py
│   ├── model_training.py
│   ├── anomaly_detection.py
│   └── visualization.py
│
├── docs
│   ├── README.md
│   ├── setup.md
│   └── usage.md
│
├── models
│   └── trained_model.h5
│
├── outputs
│   ├── figures
│   └── reports
│
└── requirements.txt
```

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/oaslananka/SmartStructureGuardian.git
    cd SmartStructureGuardian
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Simulate sensor data:
    ```bash
    python src/data_simulation.py
    ```
    This will generate simulated sensor data and save it to `data/raw/simulated_sensor_data.csv`.

2. Preprocess the sensor data:
    ```bash
    python src/data_preprocessing.py
    ```
    This will preprocess the sensor data and save it to `data/processed/preprocessed_sensor_data.csv`.

3. Train the anomaly detection model:
    ```bash
    python src/model_training.py
    ```
    This will train the anomaly detection model and save it to `models/anomaly_detection_model.pkl`.

4. Detect anomalies in the sensor data:
    ```bash
    python src/anomaly_detection.py
    ```
    This will detect anomalies in the sensor data and save the results to `outputs/reports/anomaly_detection_results.csv`.

5. Visualize the anomalies:
    ```bash
    python src/visualization.py
    ```
    This will generate a 3D animated GIF showing the bending and deformation of the bridge and save it to `outputs/figures/bridge_bending_animation.gif`.

## Visualization

The project includes scripts to visualize the sensor data and detected anomalies:

- `visualization.py`: Creates a 3D animation of the bridge deformation based on the stress data and saves it as a GIF.

Example visualization of sensor data and detected anomalies:

![Bridge Bending Animation](outputs/figures/bridge_bending_animation.gif)

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

This project was created by [oaslananka](https://github.com/oaslananka).
