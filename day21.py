"""Write a function called make_tuples that takes two lists, equal lists, and 
combines them into a list of tuples. For example, if list a is [1,2,3,4] and 
list b is [5,6,7,8], your function should return [(1,5), (2,6), (3,7), (4,8)].
"""

def make_tuples(l1, l2):
    if len(l1) != len(l2):
        return "Invalid Input"
    return list(zip(l1, l2))

print(make_tuples([1,2,3,4],[5,6,7,8] ))

"""Extra Challenge: Even Number or Average
Write a function called even_or_average that ask a user to input five numbers. 
Once the user is done, the code should return the largest even number in the 
inputted numbers. If there is no even number in the list, the code should return 
the average of all the five numbers."""

