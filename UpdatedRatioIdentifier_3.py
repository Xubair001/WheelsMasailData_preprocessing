import os
import csv
import enchant
import matplotlib.pyplot as plt

def get_language_type(paragraph):
    english_dict = enchant.Dict("en_US")

    words = paragraph.split()
    non_english_words = [word for word in words if not english_dict.check(word)]

    total_words = len(words)
    non_english_word_count = len(non_english_words)
    non_english_percentage = (non_english_word_count / total_words) * 100 if total_words > 0 else 0

    return "Roman Urdu" if non_english_percentage > 27 else "English"

def process_csv_file(csv_path):
    print(f"Processing file: {csv_path}")
    processed_rows = []
    with open(csv_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            text_data = row.get('textdata', '')
            language_type = get_language_type(text_data)
            row['LanguageType'] = language_type
            processed_rows.append(row)

    return processed_rows

def write_results(csv_path, processed_rows):
    if not processed_rows:
        print(f"No data to write in {csv_path}")
        return

    with open(csv_path, 'w', newline='') as csv_file:
        fieldnames = processed_rows[0].keys() if processed_rows else []
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(processed_rows)
        print(f"Data written to {csv_path}")

def generate_combined_pie_chart(all_processed_rows, folder_name):
    language_counts = {'English': 0, 'Roman Urdu': 0}

    for row in all_processed_rows:
        language_counts[row['LanguageType']] += 1

    total_english = language_counts['English']
    total_roman_urdu = language_counts['Roman Urdu']

    labels = [f'English ({total_english})', f'Roman Urdu ({total_roman_urdu})']
    values = [total_english, total_roman_urdu]

    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title(f'Combined Language Distribution - {folder_name}')
    plt.axis('equal') 
    plt.show()

def process_csv_folder(folder_path):
    all_processed_rows = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            csv_path = os.path.join(folder_path, filename)
            processed_rows = process_csv_file(csv_path)
            write_results(csv_path, processed_rows)
            all_processed_rows.extend(processed_rows)

    
    generate_combined_pie_chart(all_processed_rows, os.path.basename(folder_path))
    print("Script execution completed.")

def main():
    folder_path = "/home/abdullah-zubair/WheelsMasail/Web Scraping/textPreprocessing/FilteredData_Top6Posts"
    process_csv_folder(folder_path)

if __name__ == "__main__":
    main()
