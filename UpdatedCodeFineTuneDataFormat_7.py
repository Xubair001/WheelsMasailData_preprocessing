import os
import pandas as pd

def process_folder(input_folder, output_file):
    # Initialize an empty list to store formatted data
    formatted_data = []

    # Iterate through each CSV file in the folder
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.csv'):
            file_path = os.path.join(input_folder, file_name)

            # Read the CSV file into a DataFrame
            df = pd.read_csv(file_path)

            # Check if the DataFrame is not empty
            if not df.empty:
                question = df.loc[0, "textdata"]
                answers = df.loc[1:, "textdata"].tolist()

                # System message
                system_message = '{"role": "system", "content": " Welcome to WheelsMasail! Your go-to chatbot for all things related to wheels. Ask me anything about cars, maintenance, troubleshooting, or any automotive topic. I\'m here to assist you! "}'

                # User message
                user_message = '{"role": "user", "content": "' + question + '"}'

                # Assistant messages
                assistant_messages = ['{"role": "assistant", "content": ' + '"' + answer + '"}' for answer in answers]

                # Append formatted data to the list for each answer
                for assistant_message in assistant_messages:
                    formatted_data.append('{"messages": [' + system_message + ', ' + user_message + ', ' + assistant_message + ']}')

    # Write the formatted data to the output JSON file
    with open(output_file, 'w') as json_file:
        json_file.write('\n'.join([str(data) for data in formatted_data]))

    print(f"Formatted JSON file '{output_file}' created successfully!")

# Example usage:
input_folder = "/home/abdullah-zubair/WheelsMasail/Web Scraping/textPreprocessing/OUTPUT_FOLDER/finetune_data/Toyota"
output_file = "/home/abdullah-zubair/WheelsMasail/Web Scraping/textPreprocessing/Toyota_formatted.jsonl"

process_folder(input_folder, output_file)
