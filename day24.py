""""Create a function called average_calories that calculates the average calories intake 
of a user. The function should ask the user to input their calories intake for any number 
of days and once they hit ‘done’ it should calculate and return the average intake."""


def average_calories(cal, ds):
    return cal / ds


"""Write a function called nested_lists that takes any number of lists and creates a 
2-dimensional nested list of lists. For example, if you pass the following lists as arguments: 
[1, 2, 3, 5], [1, 2, 3, 4], [1, 3, 4, 5].
"""


def nested_lists(nl):
    sl = nl.split(', ')
    final = []
    for each in sl:
        final.append(each)

    return final


print(nested_lists(input()))
