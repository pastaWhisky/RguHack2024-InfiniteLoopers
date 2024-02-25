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
    
    df = pd.read_csv('Datasets/combined_cars_with_maintenance_final_corrected.csv')
    
    df['calculated_values'] = df.apply(lambda row: cost_efficiency.calculate_total_cost(budget, row['price'], years_plan, mileage_per_year, row['tax'], row['mpg'], row['MaintenanceCostYearly'], 1.5), axis=1)
    df_sorted_by_cheapest = df.sort_values(by='calculated_values', ascending=True)

    #min_row = df.loc[df['calculated_values'].idxmin()]

    min_row = df_sorted_by_cheapest.iloc[0]
    print(min_row)
    sec_min_row = df_sorted_by_cheapest.iloc[1]
    third_min_row = df_sorted_by_cheapest.iloc[2]

    
    min_attributes = min_row[['brand', 'model', 'year', 'price', 'transmission', 'mileage', 'fuelType', 'tax', 'mpg', 'engineSize']]
    sec_min_attributes = sec_min_row[['brand', 'model', 'year', 'price', 'transmission', 'mileage', 'fuelType', 'tax', 'mpg', 'engineSize']]
    third_min_attributes = third_min_row[['brand', 'model', 'year', 'price', 'transmission', 'mileage', 'fuelType', 'tax', 'mpg', 'engineSize']]
    
    
    print(min_attributes)
    print(sec_min_attributes)
    print(third_min_attributes)
    return min_attributes, sec_min_attributes, third_min_attributes 

#print(min_attributes)
