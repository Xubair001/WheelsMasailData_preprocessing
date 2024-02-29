import os
import pandas as pd
from googletrans import Translator
import nltk
from nltk.corpus import words
nltk.download('words')

english_words = set(words.words())
def is_english(word):
    return word.lower() in english_words

def is_roman_urdu(text):
    
    return any(ord(char) > 128 for char in text)

def translate_to_english(roman_urdu_text):
    if not roman_urdu_text:
        return roman_urdu_text 

    translator = Translator()
    try:
        translated = translator.translate(roman_urdu_text, src='ur', dest='en')
        return translated.text
    except Exception as e:
        print(f"Error translating '{roman_urdu_text}': {e}")
        return roman_urdu_text


def process_csv(input_file, output_folder):
    print(f"Processing file: {input_file}")
    df = pd.read_csv(input_file)
   
    df['textdata'] = df['textdata'].apply(lambda x: translate_to_english(x) if not is_english(x) or is_roman_urdu(x) else x)
    
    output_file = os.path.join(output_folder, os.path.basename(input_file))
    df.to_csv(output_file, index=False, escapechar='\\')

def process_csv_files(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    csv_files = [file for file in os.listdir(input_folder) if file.endswith('.csv')]

    for csv_file in csv_files:
        input_file = os.path.join(input_folder, csv_file)
        process_csv(input_file, output_folder)

input_folder_path = '/home/abdullah-zubair/WheelsMasail/Web Scraping/textPreprocessing/FilteredData_Top4Posts'
output_folder_path = '/home/abdullah-zubair/WheelsMasail/Web Scraping/textPreprocessing/FilteredData_Top4Posts_TranslateUrdu'
process_csv_files(input_folder_path, output_folder_path)
