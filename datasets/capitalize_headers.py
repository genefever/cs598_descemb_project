import os
import pandas as pd

def capitalize_headers(directory):
    # Loop through all files in the specified directory
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):  # Check if the file is a CSV
            file_path = os.path.join(directory, filename)
            # Read the CSV file
            df = pd.read_csv(file_path)
            # Capitalize all column headers
            df.columns = [col.upper() for col in df.columns]
            # Save the file, overwriting the original file
            df.to_csv(file_path, index=False)
            print(f'Processed {filename}')

# Specify the directory of your CSV files here
directory_path = 'data_input_path/eicu/'
capitalize_headers(directory_path)
