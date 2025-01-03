# handling large .csv files due to the github 100MB file size limitation. 
import os
import pandas as pd

def split_csv(input_file, output_dir, max_rows=500000):
    df = pd.read_csv(input_file)
    
    # Calculate the number of splits needed
    num_splits = len(df) // max_rows + (1 if len(df) % max_rows != 0 else 0)
    
    base_filename = os.path.basename(input_file)
    file_base, file_extension = os.path.splitext(base_filename)
    
    # Split and write out smaller CSVs
    for i in range(num_splits):
        split_df = df.iloc[i * max_rows : (i + 1) * max_rows]
        output_file = os.path.join(output_dir, f"{file_base}_part{i+1}{file_extension}")
        split_df.to_csv(output_file, index=False)
        print(f"Created: {output_file}")


output_directory = 'datasets/split_files'  # Directory to save split files
os.makedirs(output_directory, exist_ok=True)

# Split the two large CSV files
split_csv('datasets/Divvy_Trips_2019_Q2.csv', output_directory)
split_csv('datasets/Divvy_Trips_2019_Q3.csv', output_directory)
