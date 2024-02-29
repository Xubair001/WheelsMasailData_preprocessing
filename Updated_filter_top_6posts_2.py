import os
import pandas as pd

output_dir = '/home/abdullah-zubair/WheelsMasail/Web Scraping/textPreprocessing/PreProcessed_data'
output_filtered_dir = '/home/abdullah-zubair/WheelsMasail/Web Scraping/textPreprocessing/FilteredData_Top6Posts'

os.makedirs(output_filtered_dir, exist_ok=True)

csv_files = [file for file in os.listdir(output_dir) if file.endswith('.csv')]

for csv_file in csv_files:
    file_path = os.path.join(output_dir, csv_file)
    df = pd.read_csv(file_path)

    
    df = df[~((df['textdata'].isna()) | (df['textdata'].str.lower().str.strip() == 'textdata:'))]

    
    df['PostsCounts'] = df['PostsCounts'].str.extract(r'Posts: (\d+)').astype(int)

    
    remaining_posts_df = df.iloc[1:].nlargest(7, 'PostsCounts')

    # Concatenate the filtered DataFrame
    final_df = pd.concat([df.head(1), remaining_posts_df])

    filtered_file_path = os.path.join(output_filtered_dir, csv_file)
    final_df.to_csv(filtered_file_path, index=False, escapechar='\\')
