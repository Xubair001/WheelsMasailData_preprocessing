import os
import pandas as pd

csv_directory = '/home/abdullah-zubair/WheelsMasail/Web Scraping/textPreprocessing/FilteredData_Top6Posts'

main_csv_path = os.path.join(csv_directory, '/home/abdullah-zubair/WheelsMasail/Web Scraping/textPreprocessing/Threads_and_title.csv')
main_df = pd.read_csv(main_csv_path)

output_directory = '/home/abdullah-zubair/WheelsMasail/Web Scraping/textPreprocessing/OUTPUT_FOLDER'  # Change this to your desired output directory

finetune_folder = os.path.join(output_directory, 'finetune_data')
os.makedirs(finetune_folder, exist_ok=True)

unique_categories = main_df['Category'].unique()

for category in unique_categories:
    
    if pd.notna(category) and isinstance(category, str):
        category_folder = os.path.join(finetune_folder, str(category))
        os.makedirs(category_folder, exist_ok=True)

for index, row in main_df.iterrows():
    thread_no = row['Thread No']
    title = row['Title']
    category = row['Category']

    if pd.notna(category) and isinstance(category, str):


        csv_filename = f"thread_{thread_no}.csv"
        csv_path = os.path.join(csv_directory, csv_filename)

        if os.path.exists(csv_path):

            destination_folder = os.path.join(finetune_folder, str(category))
            destination_path = os.path.join(destination_folder, csv_filename)
            os.rename(csv_path, destination_path)
        else:
            print(f"CSV file not found for Thread No {thread_no}")

print("Organizing complete.")
