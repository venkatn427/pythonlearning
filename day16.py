"""Write a function called sum_list with one parameter that takes a nested list of integers as an 
argument and returns the sum of the integers.
For example, if you pass [[2, 4, 5, 6], [2, 3, 5, 6]] as an argument your function should return a sum of 33."""


def sum_list(n_l):
    sum = 0
    for each in n_l:
        if isinstance(each, list):
            for e in each:
                sum += int(e)
        else:
            sum += int(each)
    return sum

print(sum_list([[2, 4, 5, 6], [2, 3, 5, 6]]))

"""Nested_list = [[12, 34, 56, 67], [34, 68, 78]]
Write a code that generates a list of the following numbers from the nested list above – 34, 67, 78. 
Your output should be another list: [34, 67, 78]. The list output should not have duplicates."""


