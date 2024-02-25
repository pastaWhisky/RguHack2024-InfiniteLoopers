# Martin Meszaros
# Calculating the lowest overall cost of running a car
# 24/02/2024
# V 1.0

import cost_efficiency
import pandas as pd

def analyse_data(budget,years_plan,mileage_per_year):
    # budget = int(input("Good day User! I can help you find your next car!\nWhat's your budget(£)? >> "))
    # years_plan = int(input("How many years are you planning to keep the car for? >> "))
    # mileage_per_year = int(input("How many miles are you going to drive it in a year? >> "))
    
    df = pd.read_csv('Datasets/combined_cars.csv')
    
    df['calculated_values'] = df.apply(lambda row: cost_efficiency.calculate_total_cost(budget, row['price'], years_plan, mileage_per_year, row['tax'], row['mpg'], 1.5), axis=1)
    
    min_row = df.loc[df['calculated_values'].idxmin()]
    
    min_attributes = min_row[['brand', 'model', 'year', 'price', 'transmission', 'mileage', 'fuelType', 'tax', 'mpg', 'engineSize']]
    return min_attributes
# print(min_attributes)
