import os
import pandas as pd


output_dir = '/home/abdullah-zubair/WheelsMasail/Web Scraping/textPreprocessing/PreProcessed_data'
output_filtered_dir = '/home/abdullah-zubair/WheelsMasail/Web Scraping/textPreprocessing/Filterdata_likes_based'


os.makedirs(output_filtered_dir, exist_ok=True)


csv_files = [file for file in os.listdir(output_dir) if file.endswith('.csv')]


for csv_file in csv_files:
    file_path = os.path.join(output_dir, csv_file)
    df = pd.read_csv(file_path)
    
    
    filtered_df = df[df['likedata'].str.match(r'^\d+.*')]
    
    if not filtered_df.empty:
        
        filtered_file_path = os.path.join(output_filtered_dir, csv_file)
        filtered_df.to_csv(filtered_file_path, index=False)