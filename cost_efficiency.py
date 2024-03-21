# Martin Meszaros
# This is a module for calculating the best most viable option for a compile
# 24/02/2024
# V 1.0

import numpy as np


def calculate_total_cost(brand,budget,price,years,miles,taxpy,mpg,maintenanceyearly,costpl,manufacturers,fuel_types_checklist,fuel_types,engine_size):
    if budget >= price >= budget*0.4 and brand in manufacturers and fuel_types in fuel_types_checklist and engine_size >= 0.6:
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


