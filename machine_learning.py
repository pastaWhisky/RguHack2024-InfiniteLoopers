import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

# Step 1: Load and preprocess the dataset
# Replace 'your_data.csv' with the actual path or URL to your CSV file
df = pd.read_csv(r'Datasets/Processed_Data/combined_cars.csv')

# Assume 'df' is your preprocessed dataset
# Features are the columns that influence the cost

# Specify features
features = ['year', 'mileage', 'mpg', 'engineSize']  # Update with your actual feature names

# Step 2: Ask the user for input
budget = int(input("Enter your budget: "))
ownership_duration = int(input("Enter how many years you plan to keep the car: "))
annual_mileage = int(input("Enter how many miles you will drive it per year: "))

# Step 3: Train a model to predict the total cost of ownership
# Create a pipeline with StandardScaler and RandomForestRegressor
model = make_pipeline(StandardScaler(), RandomForestRegressor(n_estimators=100, random_state=42))

# Split the data into training and testing sets
train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)

# Fit the model on the training data
model.fit(train_data[features], train_data['price'])  # 'price' is used as a placeholder for the actual target variable

# Step 4: Recommend the best car based on the predicted total cost
# Prepare user input for prediction
user_input = pd.DataFrame({
    'price': [1],  # Replace with the actual year you are interested in
    'mpg': [200],  # Replace with the actual miles per gallon for your typical use
    'tax': [1]  # Replace with the actual engine size you are interested in
})

# Make predictions for the user input
predicted_price = model.predict(user_input)

# Calculate total cost based on predicted price and user input
#total_cost = predicted_price[0] * ownership_duration + (annual_mileage / user_input['mpg'].iloc[0]) * fuel_price_per_gallon

# Display the recommended car and cost information
print(f'Recommended Car:\n{user_input}')
print(f'\nEstimated Total Cost of Ownership over {ownership_duration} ')

