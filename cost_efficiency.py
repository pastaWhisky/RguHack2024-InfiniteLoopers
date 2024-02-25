# Martin Meszaros
# This is a module for calculating the best most viable option for a compile
# 24/02/2024
# V 1.0

import numpy as np

def calculate_total_cost(budget,price,years,miles,taxpy,mpg,maintenanceyearly,costpl):
    if budget >= price:
        mpl = mpg*(1/5.546)
        costpm = costpl/mpl
        yearly_miles_cost = costpm*miles
        total_miles_cost = yearly_miles_cost*years
        tax = taxpy*years
        total_running_cost = tax + total_miles_cost
        maintenance = maintenanceyearly*years
        total_car_cost = total_running_cost + price + maintenance

        return total_car_cost
    else:
        return np.nan


