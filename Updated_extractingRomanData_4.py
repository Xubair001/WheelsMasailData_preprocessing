import os
import pandas as pd
import regex as re

def is_roman_urdu(text):
    
    pattern = re.compile(r'^[\p{IsLatin}-]+$')
    return bool(re.match(pattern, text))

def process_csv_folder(folder_path):
    
    csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

    
    romandata_df = pd.DataFrame(columns=['CSVName', 'RowNumber', 'TextData'])

    
    for csv_file in csv_files:
        file_path = os.path.join(folder_path, csv_file)
        
        
        df = pd.read_csv(file_path)

        
        if 'LanguageType' in df.columns:
            
            roman_urdu_rows = df[df['LanguageType'] == 'Roman Urdu']

            
            romandata_df = pd.concat([
                romandata_df,
                pd.DataFrame({
                    'CSVName': [csv_file] * len(roman_urdu_rows),
                    'RowNumber': roman_urdu_rows.index + 1,
                    'TextData': roman_urdu_rows['textdata'].tolist(),
                })
            ], ignore_index=True)

            print(f"Processed {csv_file}. Roman Urdu text extracted.")
        else:
            print(f"Warning: 'LanguageType' column not found in {csv_file}.")

    
    output_file_path = 'romandata.csv'
    romandata_df.to_csv(output_file_path, index=False)

    print(f"Roman Urdu data saved to {output_file_path}")


folder_path = '/home/abdullah-zubair/WheelsMasail/Web Scraping/textPreprocessing/FilteredData_Top6Posts'
process_csv_folder(folder_path)
