import pandas as pd
import joblib # For loading the model

def predict_house_price(model_filename='house_price_model.pkl'):
    """
    Loads a pre-trained house price prediction model and makes predictions
    for new, sample house data.

    Args:
        model_filename (str): Name of the file where the trained model is saved.
    """
    print(f"--- Loading Trained Model from {model_filename} ---")
    try:
        model_pipeline = joblib.load(model_filename)
        print("Model loaded successfully.")
    except FileNotFoundError:
        print(f"Error: Model file '{model_filename}' not found. Please run 'python train_model.py' first.")
        return
    except Exception as e:
        print(f"Error loading model: {e}")
        return

    print("\n--- Making Predictions for New Houses ---")

    # Example 1: A relatively expensive house
    new_house_data_1 = pd.DataFrame({
        'SquareFeet': [2500],
        'Bedrooms': [4],
        'Bathrooms': [3],
        'YearBuilt': [2018],
        'Neighborhood': ['Central'],
        'DistanceToCityCenter': [5],
        'HasGarden': [1]
    })

    predicted_price_1 = model_pipeline.predict(new_house_data_1)[0]
    print(f"New House 1 (Central, 2500 sqft, 4/3, 2018, Garden): ${predicted_price_1:,.2f}")

    # Example 2: A moderately priced house
    new_house_data_2 = pd.DataFrame({
        'SquareFeet': [1800],
        'Bedrooms': [3],
        'Bathrooms': [2],
        'YearBuilt': [2005],
        'Neighborhood': ['West'],
        'DistanceToCityCenter': [12],
        'HasGarden': [0]
    })

    predicted_price_2 = model_pipeline.predict(new_house_data_2)[0]
    print(f"New House 2 (West, 1800 sqft, 3/2, 2005): ${predicted_price_2:,.2f}")

    # Example 3: A more affordable house
    new_house_data_3 = pd.DataFrame({
        'SquareFeet': [1200],
        'Bedrooms': [2],
        'Bathrooms': [1],
        'YearBuilt': [1990],
        'Neighborhood': ['East'],
        'DistanceToCityCenter': [20],
        'HasGarden': [0]
    })

    predicted_price_3 = model_pipeline.predict(new_house_data_3)[0]
    print(f"New House 3 (East, 1200 sqft, 2/1, 1990): ${predicted_price_3:,.2f}")


if __name__ == "__main__":
    predict_house_price()
