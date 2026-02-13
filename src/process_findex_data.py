from . import config
import pandas as pd
import os

def process_csv(raw_csv_filepath: str, processed_csv_savepath: str):
    '''This function reads in the csv as a Dataframe, removing unneeded columns, and processing it'''
    
    # read in the dataframe
    df = pd.read_csv(raw_csv_filepath)
    
    # filter out unneeded columns
    df_retained = df[config.FINDEX_COLS_TO_RETAIN]

    print(f"Checking out the csv...\n")

    print(f"{df_retained.info()}\n\n")
    
    # get data for Pakistan
    df_pakistan = df_retained[df_retained['REF_AREA_LABEL'] == 'Pakistan']
    print(f"\nSize of Pakistan-filterd dataset: {len(df_pakistan)}")
        
    # filterng out key-indicators for further analyss
    df_pakistan_filtered = df_pakistan[df_pakistan['INDICATOR_LABEL'].isin(config.FINDEX_KEY_INDICATORS)]
    print(f"Rows after filtering key indicators: {len(df_pakistan_filtered)}\n")
    
    # data checks
    print(f"\nChecking for null values:\n{df_pakistan_filtered.isna().sum()}\n")
    print(f"\nChecking for duplicate rows: {df_pakistan_filtered.duplicated().sum()}\n")
        
    # generating summary stats for numerical columns
    numerical_cols = ["TIME_PERIOD", "OBS_VALUE"]

    for col in numerical_cols:
        print(f"\nGenerating summary statistics for numerical column: {col}")
        print(df_pakistan_filtered[f"{col}"].describe())
    
    # saving processed data to data/processed
    df_pakistan_filtered.to_csv(processed_csv_savepath)
    
    
if __name__ == "__main__":
    process_csv(config.FINDEX_RAW_CSV_PATH, config.FINDEX_PROCESSED_CSV_PATH)









# df_pakistan_filtered.info()




    


# # %% [markdown]
# # ## Save to data/processed/
# # 
# # Data is clean - no nulls, no duplicates, proper data types. Ready to save.





