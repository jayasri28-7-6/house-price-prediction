--- Loading Data from house_data.csv ---
Data loaded successfully.
Dataset head:
    SquareFeet  Bedrooms  Bathrooms  YearBuilt Neighborhood  DistanceToCityCenter  HasGarden         Price
0  2049.20633         3          2       2016        North              8.423985          1  366403.957591
1  1784.85694         3          3       1984        South             11.758170          0  329598.544716
2  2450.95782         4          1       1996         East             15.827763          1  397193.303975
3  2237.28892         2          2       2001        North             10.279612          1  356407.575218
4  1978.89291         2          3       2002        South             11.795893          0  365020.916774

--- Preprocessing Data ---
Numerical features: ['SquareFeet', 'Bedrooms', 'Bathrooms', 'YearBuilt', 'DistanceToCityCenter', 'HasGarden']
Categorical features: ['Neighborhood']

--- Splitting Data into Training and Testing Sets ---
Training data shape: (800, 7), (800,)
Testing data shape: (200, 7), (200,)

--- Building and Training the Machine Learning Pipeline ---
Model training complete!

--- Evaluating the Model Performance ---
Mean Squared Error (MSE): 2470716075.76
Root Mean Squared Error (RMSE): 49706.30
R-squared (R2): 0.67

--- Saving the Trained Model to house_price_model.pkl ---
Model saved successfully.

--- Generating Visualizations ---
(A matplotlib plot window titled "Actual vs. Predicted House Prices" will appear and save `actual_vs_predicted.png`)
(Another matplotlib plot window titled "Distribution of Residuals" will appear)
