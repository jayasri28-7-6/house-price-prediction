import pandas as pd
import numpy as np

def generate_house_data(num_samples=1000, filename='house_data.csv'):
    """
    Generates a synthetic dataset for house price prediction and saves it to a CSV file.

    Args:
        num_samples (int): The number of samples (houses) to generate.
        filename (str): The name of the CSV file to save the data to.
    """
    print(f"--- Generating {num_samples} Synthetic House Data Samples ---")
    np.random.seed(42) # for reproducibility

    data = {
        'SquareFeet': np.random.normal(2000, 500, num_samples),
        'Bedrooms': np.random.randint(2, 6, num_samples),
        'Bathrooms': np.random.randint(1, 4, num_samples),
        'YearBuilt': np.random.randint(1980, 2023, num_samples),
        'Neighborhood': np.random.choice(['North', 'South', 'East', 'West', 'Central'], num_samples),
        'DistanceToCityCenter': np.random.normal(10, 5, num_samples),
        'HasGarden': np.random.choice([0, 1], num_samples, p=[0.6, 0.4]),
        'Price': 0 # Placeholder
    }

    df = pd.DataFrame(data)

    # Calculate Price based on features + noise
    df['Price'] = (
        100 * df['SquareFeet'] +
        50000 * df['Bedrooms'] +
        30000 * df['Bathrooms'] +
        1000 * (2023 - df['YearBuilt']) + # Newer homes are generally more expensive
        df['Neighborhood'].apply(lambda x: {'North': 50000, 'South': 20000, 'East': 10000, 'West': 40000, 'Central': 70000}[x]) +
        -5000 * df['DistanceToCityCenter'] + # Closer to city center is more expensive
        25000 * df['HasGarden'] +
        np.random.normal(0, 50000, num_samples) # Add random noise
    )

    # Ensure prices are positive and at a reasonable minimum
    df['Price'] = df['Price'].apply(lambda x: max(100000, x))

    df.to_csv(filename, index=False)
    print(f"Synthetic data saved to '{filename}'")
    print("Dataset head:\n", df.head())
    print("\nDataset info:\n")
    df.info()
    print("\nDataset description:\n", df.describe())

if __name__ == "__main__":
    generate_house_data()
