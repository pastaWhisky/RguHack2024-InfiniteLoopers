import pandas as pd
from fuzzywuzzy import process

# Function to get the best match for a given model
def get_best_match(model, choices):
    # You can adjust the scorer and cutoff according to your needs
    match = process.extractOne(model, choices, scorer=process.fuzz.token_sort_ratio, score_cutoff=80)
    # If a match is found with a score above the cutoff, return the matched model, else return the original
    return match[0] if match else model

# Load the datasets
df = pd.read_csv('Datasets/Car_maintenance_costs.csv')
combined_cars_df = pd.read_csv('Datasets/combined_cars.csv')

# Convert 'Make' column to lowercase and replace 'hyundi' with 'hyundai'
df['Make'] = df['Make'].str.lower().replace(r'hyundi', 'hyundai', regex=True)

# Ensure 'MaintenanceCostYearly' is a float with two decimal places
df['MaintenanceCostYearly'] = df['MaintenanceCostYearly'].astype(float).round(2)

# Strip leading/trailing whitespace and convert 'Model' column to lowercase
df['Model'] = df['Model'].str.strip().str.lower()

# Create a list of unique models from the combined_cars dataset for matching
model_choices = combined_cars_df['model'].str.lower().unique()

# Replace 'Model' entries in df with the best match from combined_cars_df
df['Model'] = df['Model'].apply(lambda x: get_best_match(x, model_choices))

# Save the modified dataframe to a new CSV file
output_file_path = 'Datasets/Modified_Car_maintenance_costsClean.csv'
df.to_csv(output_file_path, index=False)

print(f"The updated file is saved as: {output_file_path}")
