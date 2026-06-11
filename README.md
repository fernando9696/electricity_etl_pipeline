# Electricity ETL Pipeline
A basic ETL pipeline built in python that processes electricity sales and capability data from multiple file formats.

## What it does
-**Extract** - reads data from '.csv', '.parquet', and nested '.json' files
-**Transform** - Cleans and filters sales data, dropping null prices and keeping only essential data for analysis
-**Load** - Outputs the cleaned data to '.csv' or '.parquet' files

## Tech Stack
-Python
-Pandas

## How to run
1. Clone the repo
   git clone https://github.com/fernando9696/electricity_etl_pipeline.git

2. Install dependencies
   pip install pandas pyarrow

3. Run the pipeline
   python pipeline.py

