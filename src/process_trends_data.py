from . import config
import pandas as pd
import os

def process_csv(raw_csv_filepaths: dict, processed_dir: str):
    '''This function processes Google Trends CSVs and saves separate files per category'''
    
    # create processed directory
    os.makedirs(processed_dir, exist_ok=True)
    
    # read and process each category of trends data
    for category, filepath in raw_csv_filepaths.items():
        
        print(f"Reading from {filepath}...")
        df = pd.read_csv(filepath)
        
        # remove isPartial col (redundant column)
        if 'isPartial' in df.columns:
            df = df.drop('isPartial', axis=1)
        
        # data quality checks
        print(f"\nChecking for null values:\n{df.isna().sum()}\n")
        print(f"Checking for duplicate rows: {df.duplicated().sum()}\n")
        
        # handle missing values if any
        null_count = df.isna().sum().sum()
        if null_count > 0:
            print(f"Handling {null_count} missing values by filling with 0")
            df = df.fillna(0)
        
        # remove duplicates if any
        dup_count = df.duplicated().sum()
        if dup_count > 0:
            print(f"Removing {dup_count} duplicate rows")
            df = df.drop_duplicates()
        
        # standardize date format
        print(f"Converting 'date' column to datetime format...")
        df['date'] = pd.to_datetime(df['date'])
        
        # sort by date for time-series analysis
        df = df.sort_values('date').reset_index(drop=True)
        
        # generating summary statistics for numerical columns
        numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
        
        for col in numerical_cols:
            print(f"\nSummary statistics for {col}:")
            print(df[col].describe())
        
        # save processed csv for this category
        output_path = f"{processed_dir}/trends_{category}.csv"
        df.to_csv(output_path)
    


if __name__ == "__main__":
    process_csv(config.TRENDS_RAW_CSV_PATHS, config.TRENDS_PROCESSED_CSV_DIR)
