# Martin Meszaros
# Calculating the lowest overall cost of running a car
# 24/02/2024
# V 1.1

import cost_efficiency
import pandas as pd


def analyse_data(budget,years_plan,mileage_per_year,manufacturers,fuel_types_checklist):
    # budget = int(input("Good day User! I can help you find your next car!\nWhat's your budget(£)? >> "))
    # years_plan = int(input("How many years are you planning to keep the car for? >> "))
    # mileage_per_year = int(input("How many miles are you going to drive it in a year? >> "))
     
    df = pd.read_csv('Datasets/Processed_Data/used_car_data_combined.csv')

    # pull petrol and diesel
    df2 = pd.read_excel('Datasets/Provided_Datasets/used-car-dataset-challenge/Fuel_Prices_and_Conversions.xlsx')

    petrol_cost = df2.loc[df2['Fuel'] == 'Petrol', 'Cost'].values[0]
    diesel_cost = df2.loc[df2['Fuel'] == 'Diesel', 'Cost'].values[0]


    # Hybrid fuel will default to petrol price, only diesel has different
    if (df['fuelType'].values[0] == 'Diesel'): 
        fuel_cost = diesel_cost
    else:
        fuel_cost = petrol_cost


    
    df['calculated_values'] = df.apply(lambda row: cost_efficiency.calculate_total_cost(row['brand'],budget, row['price'], years_plan, mileage_per_year, row['tax'], row['mpg'], row['MaintenanceCostYearly'], fuel_cost,manufacturers,fuel_types_checklist,row['fuelType']), axis=1)
    df_sorted_by_cheapest = df.sort_values(by='calculated_values', ascending=True)

    #min_row = df.loc[df['calculated_values'].idxmin()]
    
    car_options = []
    for i in range(100):
        car_data = df_sorted_by_cheapest.iloc[i]
        car_options.append(car_data[['brand', 'model', 'year', 'price', 'transmission', 'mileage', 'fuelType', 'tax', 'mpg', 'engineSize']])

    # min_row = df_sorted_by_cheapest.iloc[0]
    # sec_min_row = df_sorted_by_cheapest.iloc[1]
    # third_min_row = df_sorted_by_cheapest.iloc[2]
    # 
    # min_attributes = min_row[['brand', 'model', 'year', 'price', 'transmission', 'mileage', 'fuelType', 'tax', 'mpg', 'engineSize']]
    # sec_min_attributes = sec_min_row[['brand', 'model', 'year', 'price', 'transmission', 'mileage', 'fuelType', 'tax', 'mpg', 'engineSize']]
    # third_min_attributes = third_min_row[['brand', 'model', 'year', 'price', 'transmission', 'mileage', 'fuelType', 'tax', 'mpg', 'engineSize']]
    
#    return min_attributes, sec_min_attributes, third_min_attributes
    return car_options
#print(min_attributes)
