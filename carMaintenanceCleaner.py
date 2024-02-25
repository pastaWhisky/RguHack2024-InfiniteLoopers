import pandas as pd

# Load the dataset
df = pd.read_csv('Datasets/Car_maintenance_costs.csv')

# Convert 'Make' column to lowercase and replace 'hyundi' with 'hyundai'
df['Make'] = df['Make'].str.lower().str.replace(r'hyundi', 'hyundai', regex=True)

# Ensure 'MaintenanceCostYearly' is a float with two decimal places
df['MaintenanceCostYearly'] = df['MaintenanceCostYearly'].astype(float).round(2)

# Strip leading/trailing whitespace and convert 'Model' column to lowercase
df['Model'] = df['Model'].str.strip().str.lower()

# Save the modified dataframe to a new CSV file
output_file_path = 'Datasets/Modified_Car_maintenance_costsClean.csv'
df.to_csv(output_file_path, index=False)

output_file_path


from fuzzywuzzy import process
import pandas as pd

# Load your dataframes (assuming you have them as 'combined_cars_df' and 'maintenance_costs_df')

# Function to get the best match for a given model
def get_best_match(model, choices, scorer, cutoff):
    match = process.extractOne(model, choices, scorer=scorer, score_cutoff=cutoff)
    return match[0] if match else None

# List of choices to match against (unique models from 'combined_cars.csv')
model_choices = combined_cars_df['model'].unique()

# Apply the function to the 'Model' column in 'maintenance_costs_df'
# You can adjust the scorer and cutoff according to your needs
maintenance_costs_df['Model'] = maintenance_costs_df['Model'].apply(
    lambda x: get_best_match(x, model_choices, scorer=fuzzywuzzy.fuzz.partial_ratio, cutoff=90)
)

# Now 'maintenance_costs_df' has 'Model' column updated with the best match from 'combined_cars_df'
# You can then save this dataframe to a new CSV file
maintenance_costs_df.to_csv('Updated_Maintenance_Costs.csv', index=False)