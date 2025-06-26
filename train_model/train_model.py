import pandas as pd
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_squared_error, r2_score
    from sklearn.preprocessing import StandardScaler, OneHotEncoder
    from sklearn.compose import ColumnTransformer
    from sklearn.pipeline import Pipeline
    import matplotlib.pyplot as plt
    import seaborn as sns
    import joblib # For saving/loading the model

    def train_and_evaluate_model(data_path='house_data.csv', model_filename='house_price_model.pkl'):
        """
        Loads data, preprocesses it, trains a linear regression model,
        evaluates its performance, and saves the trained model.

        Args:
            data_path (str): Path to the CSV file containing the house data.
            model_filename (str): Name of the file to save the trained model.
        """
        print(f"--- Loading Data from {data_path} ---")
        try:
            df = pd.read_csv(data_path)
            print("Data loaded successfully.")
            print("Dataset head:\n", df.head())
        except FileNotFoundError:
            print(f"Error: Data file '{data_path}' not found. Please run 'python data_generator.py' first.")
            return

        # --- 1. Data Preprocessing ---
        print("\n--- Preprocessing Data ---")

        X = df.drop('Price', axis=1)
        y = df['Price']

        numerical_features = X.select_dtypes(include=np.number).columns.tolist()
        categorical_features = X.select_dtypes(include='object').columns.tolist()

        print(f"Numerical features: {numerical_features}")
        print(f"Categorical features: {categorical_features}")

        # Create preprocessing pipelines for numerical and categorical features
        numerical_transformer = Pipeline(steps=[
            ('scaler', StandardScaler())
        ])

        categorical_transformer = Pipeline(steps=[
            ('onehot', OneHotEncoder(handle_unknown='ignore'))
        ])

        # Combine transformers using ColumnTransformer
        preprocessor = ColumnTransformer(
            transformers=[
                ('num', numerical_transformer, numerical_features),
                ('cat', categorical_transformer, categorical_features)
            ])

        # --- 2. Split Data ---
        print("\n--- Splitting Data into Training and Testing Sets ---")
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        print(f"Training data shape: {X_train.shape}, {y_train.shape}")
        print(f"Testing data shape: {X_test.shape}, {y_test.shape}")

        # --- 3. Create and Train the Model Pipeline ---
        print("\n--- Building and Training the Machine Learning Pipeline ---")
        model_pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                                         ('regressor', LinearRegression())])

        model_pipeline.fit(X_train, y_train)
        print("Model training complete!")

        # --- 4. Evaluate the Model ---
        print("\n--- Evaluating the Model Performance ---")
        y_pred = model_pipeline.predict(X_test)

        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, y_pred)

        print(f"Mean Squared Error (MSE): {mse:.2f}")
        print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
        print(f"R-squared (R2): {r2:.2f}")

        # --- 5. Save the Trained Model ---
        print(f"\n--- Saving the Trained Model to {model_filename} ---")
        joblib.dump(model_pipeline, model_filename)
        print("Model saved successfully.")

        # --- 6. Visualizations ---
        print("\n--- Generating Visualizations ---")

        # Plotting actual vs. predicted prices
        plt.figure(figsize=(10, 6))
        sns.regplot(x=y_test, y=y_pred, scatter_kws={'alpha':0.3}, line_kws={'color':'red'})
        plt.xlabel("Actual Prices ($)")
        plt.ylabel("Predicted Prices ($)")
        plt.title("Actual vs. Predicted House Prices")
        plt.grid(True)
        plt.savefig('actual_vs_predicted.png') # <--- Moved this line here
        plt.show()

        # Plotting residuals
        residuals = y_test - y_pred
        plt.figure(figsize=(10, 6))
        sns.histplot(residuals, kde=True)
        plt.xlabel("Residuals (Actual - Predicted)")
        plt.ylabel("Frequency")
        plt.title("Distribution of Residuals")
        plt.grid(True)
        plt.show() # You can add plt.savefig() here too if you want to save this plot
    if __name__ == "__main__":
        train_and_evaluate_model()
    
