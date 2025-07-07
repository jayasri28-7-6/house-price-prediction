# House Price Prediction

**Internship Details:**
* **Company:** CODTECH IT SOLUTIONS
* **Name:** Jayasri N
* **Intern ID:** CT04DG1603
* **Domain:** Data Analytics
* **Duration:** 4 Weeks
* **Mentor:** Neela Santosh kumar

This project implements a machine learning pipeline for predicting house prices. It covers data generation, preprocessing, model training, evaluation, and making new predictions.

## Features

* **Synthetic Data Generation**: Creates a sample dataset of house features and prices.
* **Data Preprocessing**: Handles numerical scaling and categorical encoding.
* **Linear Regression Model**: Trains a linear regression model for price prediction.
* **Model Evaluation**: Calculates Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and R-squared (R2).
* **Model Persistence**: Saves the trained model for future use.
* **Prediction**: Loads the saved model to predict prices for new data.
* **Basic Visualizations**: Plots actual vs. predicted prices and residual distribution.

## Model Performance Visualization

A visualization showing actual house prices against predicted prices. Points should ideally fall close to the red regression line.

## Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

* Python 3.8+
* `pip` (Python package installer)

### Installation

1.  **Clone the repository (or download the files):**
    ```bash
      https://github.com/YOUR_USERNAME/house-price-prediction.git
    ```
    *(Note: Replace `YOUR_USERNAME` with your actual GitHub username and adjust the repo name if it's different)*

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    * **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    * **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

### How to Run

1.  **Generate the dataset:**
    This script creates `house_data.csv`.
    ```bash
    python data_generator.py
    ```

2.  **Train the model:**
    This script preprocesses data, trains, evaluates, generates plots, and saves `house_price_model.pkl`.
    ```bash
    python train_model.py
    ```

3.  **Make predictions:**
    Loads the saved model to predict prices for new data.
    ```bash
    python predict_price.py
    ```

## Project Structure
```
house-price-prediction/
├── README.md
├── requirements.txt
├── data_generator.py
├── train_model.py
├── predict_price.py
├── house_data.csv         
```
## Dependencies

All dependencies are listed in `requirements.txt`.

## Future Enhancements

* **Real Dataset**: Integrate a real-world house price dataset.
* **More Models**: Experiment with other regression algorithms.
* **Feature Engineering**: Create more informative features.
* **Hyperparameter Tuning**: Optimize model performance.
* **Web Application**: Build a simple web interface for predictions.
