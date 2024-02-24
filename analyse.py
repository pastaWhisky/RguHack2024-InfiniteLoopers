# Martin Meszaros
# Calculating the lowest overall cost of running a car
# 24/02/2024
# V 1.0

import cost_efficiency
import pandas as pd

df = pd.read_csv('Datasets/combined_cars.csv')

df['calculated_values'] = df.apply(lambda row: cost_efficiency.calculate_total_cost(row['price'], 100, 100000, row['tax'], row['mpg'], 1.5), axis=1)

min_row = df.loc[df['calculated_values'].idxmin()]

min_attributes = min_row[['brand', 'model', 'year', 'price', 'transmission', 'mileage', 'fuelType', 'tax', 'mpg', 'engineSize']]

print(min_attributes)
