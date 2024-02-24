# Martin Meszaros
# This is a module for calculating the best most viable option for a compile
# 24/02/2024
# V 1.0

def calculate_total_cost(price,years,miles,taxpy,mpg,costpl):
    mpl = mpg*(1/5.546)
    costpm = costpl*mpl
    yearly_miles_cost = costpm*miles
    total_miles_cost = yearly_miles_cost*years
    tax = taxpy*years
    total_running_cost = tax + total_miles_cost
    total_car_cost = total_running_cost + price

    return total_car_cost

