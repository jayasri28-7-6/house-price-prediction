--- Generating 1000 Synthetic House Data Samples ---
Synthetic data saved to 'house_data.csv'
Dataset head:
    SquareFeet  Bedrooms  Bathrooms  YearBuilt Neighborhood  DistanceToCityCenter  HasGarden         Price
0  2049.20633         3          2       2016        North              8.423985          1  366403.957591
1  1784.85694         3          3       1984        South             11.758170          0  329598.544716
2  2450.95782         4          1       1996         East             15.827763          1  397193.303975
3  2237.28892         2          2       2001        North             10.279612          1  356407.575218
4  1978.89291         2          3       2002        South             11.795893          0  365020.916774

Dataset info:

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1000 entries, 0 to 999
Data columns (total 8 columns):
 #   Column                Non-Null Count  Dtype  
---  ------                --------------  -----  
 0   SquareFeet            1000 non-null   float64
 1   Bedrooms              1000 non-null   int64  
 2   Bathrooms             1000 non-null   int64  
 3   YearBuilt             1000 non-null   int64  
 4   Neighborhood          1000 non-null   object 
 5   DistanceToCityCenter  1000 non-null   float64
 6   HasGarden             1000 non-null   int64  
 7   Price                 1000 non-null   float64
dtypes: float64(3), int64(4), object(1)
memory usage: 62.6+ KB

Dataset description:
         SquareFeet     Bedrooms  Bathrooms    YearBuilt  DistanceToCityCenter    HasGarden           Price
count  1000.000000  1000.000000  1000.000000  1000.000000           1000.000000  1000.000000     1000.000000
mean   2000.803730     3.490000     1.996000  2001.402000              9.957199     0.407000   326792.204555
std     494.671077     1.121404     0.820256    12.441434              5.187313     0.491494    85579.034789
min     541.977461     2.000000     1.000000  1980.000000             -4.542095     0.000000   100000.000000
25%    1656.702206     2.000000     1.000000  1990.000000              6.467406     0.000000   265902.932975
50%    1983.355209     3.000000     2.000000  2002.000000              9.907997     0.000000   324424.939223
75%    2343.344445     4.000000     3.000000  2012.000000             13.435422     1.000000   385203.468205
max    3704.921385     5.000000     3.000000  2022.000000             27.606362     1.000000   664972.164539
