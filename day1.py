"""Write a function called divide_or_square that takes one argument (a number), 
and returns the square root of the number if it is divisible by 5, 
returns its remainder if it is not divisible by 5. For example, 
if you pass 10 as an argument, then your function should return 3.16 as the square root."""

import math

def divide_or_square(num):
    rem = num % 5
    if rem == 0:
        return math.sqrt(num)
    else:
        return round(rem, 2)
    
    
print(divide_or_square(10))


"""Write a function called longest_value that takes a 
dictionary as an argument and returns the first longest 
value of the dictionary. For example, the following 
dictionary should return – apple as the longest value.
fruits = {'fruit': 'apple', 'color': 'green'}
"""

def longest_value(fruits):
    l = 0
    for key, value in fruits.items():
        if l < len(value):
            first_lon = value
            l = len(value)
        else:
            continue
    return first_lon
    
fruits = {'fruit': 'apple', 'color': 'grreen','size': 'green'}

print(longest_value(fruits=fruits))        