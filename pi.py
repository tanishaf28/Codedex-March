"""
Pi Day 🥧 - Daily Coding Challenge

It's March 14... Pi Day! Time to celebrate the math constant π (pi).

You and your friends are sharing a delicious pie at a bakery. 
You know the diameter of the pie and the number of friends.

The pie needs to be cut into slices so everyone gets a piece.

Task:
Complete the function that calculates how much crust (circumference)
each friend gets if the pie slices are shared evenly.

Steps:
1. Use π in Python.
2. Calculate the circumference of the pie.
3. Divide the circumference evenly among friends.
4. Return the crust per friend rounded to 2 decimal places.

Formula:
C = π × d

Where:
C = circumference
d = diameter of the pie

Example 1
Input:
diameter = 10
friends = 8
Output:
3.93

Example 2
Input:
diameter = 12
friends = 5
Output:
7.54
"""

import math

def crust_per_friend(diameter, friends):
    circumference = math.pi * diameter
    crust = circumference / friends
    return round(crust, 2)


# Test cases
print(crust_per_friend(10, 8))  # 3.93
print(crust_per_friend(12, 5))  # 7.54
