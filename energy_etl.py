import pandas as pd
import json

# Extracting data from .csv and .parquet files
def extract_tabular_data(file_path: str):
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
        return df
    elif file_path.endswith('.parquet'):
        df = pd.read_parquet(file_path)
        return df
    else:
        print(f'Warning: Invalid file extension. Please try with .csv or .parquet!')
        return None# Extract and flatten data from JSON file

def extract_json_data(file_path):
    with open(file_path, 'r') as json_file:
        raw_data = json.load(json_file)
    
    data = pd.json_normalize(raw_data)
    
    return data

# With the data imported, the data must be cleaned and transformed
def transform_electricity_sales_data(raw_data: pd.DataFrame):
    # Drop any records with NA values in the `price` column
    raw_data.dropna(subset=['price'], inplace=True)
    
    # Only keep records with a `sectorName` of "residential" or "transportation"
    clean_data = raw_data.loc[raw_data['sectorName'].isin(['residential', 'transportation']), :].copy()
    
    # Create a `month` and year column using the first 4 char in 'period' and last 2 in 'year'
    clean_data['month'] = clean_data['period'].str[0:4]
    clean_data['year'] = clean_data['period'].str[5:]
    
    # Keep only the columns `year`, `month`, `stateid`, `price` and `price-units` and return dataframe
    clean_data = clean_data.loc[:, ['year', 'month', 'stateid', 'price', 'price-units']]
    
    return clean_data# Load DataFrame to .csv or .parquet file

def load(dataframe: pd.DataFrame, file_path: str):
    if file_path.endswith('.csv'):
        dataframe.to_csv(file_path, index=False)
    elif file_path.endswith('.parquet'):
        dataframe.to_parquet(file_path)
    else:
        print(f'Warning: {file_path} is not a valid file type. Please try again!')
        

# Extract data from files
raw_electricity_capability_df = extract_json_data("electricity_capability_nested.json")
raw_electricity_sales_df = extract_tabular_data("electricity_sales.csv")

# Transfrom data
cleaned_electricity_sales_df = transform_electricity_sales_data(raw_electricity_sales_df)

# Load transformed data into .csv and .parquet files
load(raw_electricity_capability_df, "loaded__electricity_capability.parquet")
load(cleaned_electricity_sales_df, "loaded__electricity_sales.csv")