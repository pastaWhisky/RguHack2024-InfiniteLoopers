import pandas as pd
import glob

# Path to the directory containing CSV files
directory_path = 'path/to/your/csv/directory/'

# Create a pattern to match all CSV files in the directory
csv_pattern = directory_path + '*.csv'

# Use glob to find all file paths matching the pattern
csv_files = glob.glob(csv_pattern)

# Combine CSV files
combined_csv = pd.concat([pd.read_csv(f) for f in csv_files])

# Optional: If you want to ignore the index or want a continuous index in the combined file
combined_csv.reset_index(drop=True, inplace=True)

# Save the combined CSV to a new file
combined_csv.to_csv(directory_path + 'combined.csv', index=False)
