import pandas as pd
import glob
import sys
import os

def merge_csv_files(start, end):
    # Get list of all CSV files in current directory
    csv_files = glob.glob('*.csv')
    print(csv_files)
    
    # Create empty list to store dataframes
    df_list = []
    
    # Read each CSV file and append to list
    for file in csv_files:
        df = pd.read_csv(file)
        df_list.append(df)
    
    # Concatenate all dataframes
    merged_df = pd.concat(df_list, ignore_index=True)

    # Drop specified columns from merged dataframe
    merged_df = merged_df.drop(['custom_metadata', 'metadata_stream', 'page_rotation'], axis=1)
    
    # Create output filename using start and end variables
    output_file = f'GOVDocs_{start}_to_{end}.csv'

    # Remove original CSV files from start to end range
    for i in range(int(start), int(end)+1):
        filename = f'GOVDoc{i}.csv'
        try:
            os.remove(filename)
            print(f"Removed {filename}")
        except OSError as e:
            print(f"Error removing {filename}: {e}")
    
    # Save merged dataframe to CSV
    merged_df.to_csv(output_file, index=False)
    print(f"CSV files merged successfully into {output_file}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py start end")
        sys.exit(1)
        
    start = sys.argv[1]
    end = sys.argv[2]
    
    merge_csv_files(start, end)
