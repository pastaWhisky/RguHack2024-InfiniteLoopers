import pandas as pd

# Load the newly uploaded CSV files to compare their 'Model' columns
combined_cars_df = pd.read_csv('/mnt/data/combined_cars.csv')
modified_maintenance_costs_df = pd.read_csv('/mnt/data/Modified_Car_maintenance_costsClean.csv')

# Display the first few rows of each DataFrame to understand their structure
combined_cars_df.head(), modified_maintenance_costs_df.head()


from thefuzz import process

# Standardizing the case for comparison - using the title case for both
combined_cars_df['model'] = combined_cars_df['model'].str.title()
modified_maintenance_costs_df['Model'] = modified_maintenance_costs_df['Model'].str.title()

# Getting a unique list of models from both DataFrames for better performance in matching
unique_combined_models = combined_cars_df['model'].unique()
unique_modified_models = modified_maintenance_costs_df['Model'].unique()

# Dictionary to hold the closest matches
closest_matches = {}

# Finding the closest match for each unique model in the modified maintenance costs DataFrame
for mod_model in unique_modified_models:
    closest_match = process.extractOne(mod_model, unique_combined_models, score_cutoff=80)
    if closest_match:
        closest_matches[mod_model] = closest_match[0]

# Displaying the matches found to review before applying changes
closest_matches

