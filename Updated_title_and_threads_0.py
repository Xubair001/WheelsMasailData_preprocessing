import pandas as pd
import os
import re


def split_text(input_file, output_file):
    with open(input_file, 'r') as file:
        content = file.read()

    threads = re.split(r'~~~~', content)

    thread_data = []
    thread_no = None
    for thread in threads:
        if thread.strip():
            thread_no_match = re.search(r'THREAD #(\d+)', thread)
            if thread_no_match:
                thread_no = thread_no_match.group(1)
            title, category = get_thread_title_and_category(thread)
            thread_dict = {"Thread No": thread_no, "Title": title, "Category": category}
            thread_data.append(thread_dict)

    thread_data = [thread for thread in thread_data if thread["Title"] != ""]

    df = pd.DataFrame(thread_data)
    df.to_csv(output_file, index=False)

def get_thread_title_and_category(thread_content):
    title_match = re.search(r'Title:(.*?)(?=(Post:|~~~~))', thread_content, re.DOTALL)
    if title_match:
        title = title_match.group(1).strip()

        # Splitting using the first two splitters "|~~|~~|"
        title_parts = title.split('|~~|~~|', 2)
        if len(title_parts) >= 2:
            title = title_parts[0].strip()
            category = title_parts[1].strip().lstrip('~|')  # Remove leading ~~|
        else:
            category = ""

        return title, category
    else:
        return "", ""

if __name__ == "__main__":
    input_file = '/home/abdullah-zubair/WheelsMasail/Web Scraping/textPreprocessing/WheelsMasail_Data.txt'
    output_file = '/home/abdullah-zubair/WheelsMasail/Web Scraping/textPreprocessing/Threads_and_title.csv'

    split_text(input_file, output_file)
