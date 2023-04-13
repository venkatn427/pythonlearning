"""
Write a function called register_check that checks
how many students are in school. The function takes a 
dictionary as a parameter. If the student is in school, 
the dictionary says ‘yes’. If the student is not in school, 
the dictionary says ‘no’. Your function should return the 
number of students in school. 
Use the dictionary below. Your function should return 3.
"""

register = {'Michael':'yes','John': 'no', 
            'Peter':'yes', 'Mary': 'yes'}


def register_check(dct):
    cnt = 0
    for k, v in dct.items():
        if v == 'yes':
            cnt += 1 
        else:
            continue
    return cnt

print(register_check(register))

"""
You are given a list of names above. This list is made up 
of names of lowercase and uppercase letters. Your task is 
to write a code that will return a tuple of all the names 
in the list that have only lowercase letters. Your tuple 
should have names sorted alphabetically in descending order.
"""

def check_lower(names):
    lower = []
    for each in names:
        if each.islower():
            lower.append(each)
        else:
            continue
        
    return set(lower)

names = ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]

print(check_lower(names))
            