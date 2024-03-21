# Martin Meszaros
# Calculating the lowest overall cost of running a car
# 24/02/2024
# V 1.1

import cost_efficiency
import pandas as pd
import numpy

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


    
    df['calculated_values'] = df.apply(lambda row: cost_efficiency.calculate_total_cost(row['brand'],budget, row['price'], years_plan, mileage_per_year, row['tax'], row['mpg'], row['MaintenanceCostYearly'], fuel_cost,manufacturers,fuel_types_checklist,row['fuelType'],row['engineSize']), axis=1)
    df_sorted_by_cheapest = df.sort_values(by='calculated_values', ascending=True)

    #min_row = df.loc[df['calculated_values'].idxmin()]
    fuzzy_weights = []
    car_options = []
    for i in range(100):
        car_data = df_sorted_by_cheapest.iloc[i]
        cost_weight = 100-i
        age_weight = 15*(50-(2020-car_data['year']))
        review_weight = 3*(10*car_data['rating'])
        if 0 < car_data['mileage'] < 10000:
            mileage_weight = 100
        elif 10000 <= car_data['mileage'] < 20000:
            mileage_weight = 90
        elif 20000 <= car_data['mileage'] < 30000:
            mileage_weight = 80
        elif 30000 <= car_data['mileage'] < 40000:
            mileage_weight = 70
        elif 40000 <= car_data['mileage'] < 50000:
            mileage_weight = 60
        elif 50000 <= car_data['mileage'] < 60000:
            mileage_weight = 50
        elif 60000 <= car_data['mileage'] < 70000:
            mileage_weight = 40
        elif 70000 <= car_data['mileage'] < 80000:
            mileage_weight = 30
        elif 80000 <= car_data['mileage'] < 90000:
            mileage_weight = 20
        elif 90000 <= car_data['mileage'] < 100000:
            mileage_weight = 10
        else:
            mileage_weight = 0

        fuzzy = cost_weight + age_weight + review_weight + mileage_weight*3
        fuzzy_weights.append(fuzzy)
    
        car_options.append(car_data[['brand', 'model', 'year', 'price', 'transmission', 'mileage', 'fuelType', 'tax', 'mpg', 'engineSize', 'rating']])
        #car_options.append(car_data[['brand', 'model', 'year', 'price', 'transmission', 'mileage', 'fuelType', 'tax', 'mpg', 'engineSize', 'rating', 'weight']])
    #sorted_by_weight = car_options.sort_values(by='weight', ascending=False)
    #cars_weighted = []

    calc_weight = numpy.array(fuzzy_weights)
    #sort_index = numpy.argsort(calc_weight)
    sort_index = [i for i, x in sorted(enumerate(calc_weight), key=lambda x: x[1])]
    cars_fuzzy = []
    #print(sort_index)
    for i in range(100):
        current_value = sort_index.index(99-i)
        cars_fuzzy.append(car_options[current_value])
        #cars_fuzzy[sort_index[i]] = car_options[sort_index[i]] 
    # min_row = df_sorted_by_cheapest.iloc[0]
    # sec_min_row = df_sorted_by_cheapest.iloc[1]
    # third_min_row = df_sorted_by_cheapest.iloc[2]
    # 
    # min_attributes = min_row[['brand', 'model', 'year', 'price', 'transmission', 'mileage', 'fuelType', 'tax', 'mpg', 'engineSize']]
    # sec_min_attributes = sec_min_row[['brand', 'model', 'year', 'price', 'transmission', 'mileage', 'fuelType', 'tax', 'mpg', 'engineSize']]
    # third_min_attributes = third_min_row[['brand', 'model', 'year', 'price', 'transmission', 'mileage', 'fuelType', 'tax', 'mpg', 'engineSize']]
    
#    return min_attributes, sec_min_attributes, third_min_attributes
    #return car_options
    return cars_fuzzy
#print(min_attributes)
