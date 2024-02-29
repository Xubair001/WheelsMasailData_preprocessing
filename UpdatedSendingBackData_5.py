import os
import pandas as pd

def revert_changes(folder_path, romandata_path):
    romandata_df = pd.read_csv(romandata_path)

    for _, row in romandata_df.iterrows():
        csv_file = row['CSVName']
        row_number = int(row['RowNumber']) - 1  

        csv_file_path = os.path.join(folder_path, csv_file)

        
        if not os.path.exists(csv_file_path):
            print(f"Warning: CSV file not found - {csv_file_path}")
            continue

        original_df = pd.read_csv(csv_file_path)

        
        if 'textdata' not in original_df.columns:
            print(f"Error: 'textdata' column not found in {csv_file}")
            continue

        original_df.at[row_number, 'textdata'] = row['TextData']

        
        original_df.to_csv(csv_file_path, index=False)

        print(f"Reverted {csv_file}. Row {row_number + 1} with Roman Urdu text.")

    print("Reverted changes back to original CSV files.")

folder_path = '/home/abdullah-zubair/WheelsMasail/Web Scraping/textPreprocessing/FilteredData_Top6Posts'
romandata_path = '/home/abdullah-zubair/WheelsMasail/Web Scraping/textPreprocessing/modified_corrected.csv'

revert_changes(folder_path, romandata_path)
