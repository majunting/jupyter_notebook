# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 09:56:43 2020

@author: juntingma
"""
import numpy as np

"""
# part A - house hunting
portion_down_payment = 0.25
current_saving= 0.0
annual_return = 0.04
monthly_return = annual_return / 12

annual_salary = float(input("Enter your annual salary:"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost = float(input("Enter the cost of your dream house:"))

number_of_months= 0
monthly_salary = annual_salary / 12
down_payment = portion_down_payment * total_cost

while (current_saving < down_payment):
    number_of_months += 1
    current_saving *= 1 + monthly_return
    current_saving += monthly_salary * portion_saved
print("Number of months:", number_of_months)
"""

"""
# part B - saving, with a raise
portion_down_payment = 0.25
current_saving= 0.0
annual_return = 0.04
monthly_return = annual_return / 12

annual_salary = float(input("Enter your annual salary:"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost = float(input("Enter the cost of your dream house:"))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal:"))

number_of_months= 0
monthly_salary = annual_salary / 12
down_payment = portion_down_payment * total_cost

while (current_saving < down_payment):
    if (number_of_months != 0 and number_of_months % 6 == 0):
        annual_salary *= 1 + semi_annual_raise
        monthly_salary = annual_salary / 12
    number_of_months += 1
    current_saving *= 1 + monthly_return
    current_saving += monthly_salary * portion_saved
print("Number of months:", number_of_months)
"""

# part C - finding the right amount to save away
semi_annual_raise = 0.07
annual_return = 0.04
portion_down_payment = 0.25

total_cost = 1000000
number_of_months = 36
min_percentage = 1
max_percentage = 10000

monthly_return = annual_return / 12
down_payment = portion_down_payment * total_cost

annual_salary = float(input("Enter the starting salary:"))

def check_percentage(percentage):
    current_saving = 0
    monthly_salary = annual_salary / 12
    for month in range(number_of_months):
        if month != 0 and month % 6 == 0:
            monthly_salary *= 1 + 0.07
        current_saving *= 1 + monthly_return
        current_saving += monthly_salary * float(percentage) / 10000
        
    if current_saving > down_payment + 100:
        return 2
    elif current_saving < down_payment - 100:
        return 0
    else:
        return 1
        
possible = False
num_iteration = 0
curr_percentage = 0

while True:
    num_iteration += 1
    prev_percentage = curr_percentage
    curr_percentage = int((min_percentage + max_percentage) / 2)
    check_result = check_percentage(curr_percentage)
    if check_result == 0:
        min_percentage = curr_percentage
    elif check_result == 2:
        max_percentage = curr_percentage
    else:
        possible = True
        break
    # min_percentage and max_percentage stuck if mean does not change
    if prev_percentage == curr_percentage:
        break

if possible:
    print("Best savings rate:" + str(curr_percentage / 10000))
    print("Steps in bisection search:", num_iteration)
else:
    print("It is not possible to pay the down payment in three years.")