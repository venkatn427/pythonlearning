"""
Write a function called convert_add that takes a 
list of strings as an argument and converts it to integers
and sums the list. For example [‘1’, ‘3’, ‘5’] should be 
converted to [1, 3, 5] and summed to 9.
"""


def convert_add(num):
    new = []
    for each in num:
        new.append(int(each))
    return new


print(convert_add(['1', '2', '3']))

"""
Write a function called check_duplicates that takes a 
list of strings as an argument. The function should check 
if the list has any duplicates. If there are duplicates, 
the function should return the duplicates. 
If there are no duplicates, the function should return 
"No duplicates". For example, the list of fruits below 
should return apple as a duplicate and list of names 
should return "no duplicates".
"""


def check_duplicates(fruits):
    dup = []
    seen = []
    for each in fruits:
        if each in seen:
            dup.append(each)
        else:
            seen.append(each)

    if len(dup) == 0:
        return "no duplicates"
    else:
        return dup


fruits = ['apple', 'orange', 'banana', 'apple']
names = ['Yoda', 'Moses', 'Joshua', 'Mark']

print(check_duplicates(fruits=fruits))
print(check_duplicates(fruits=names))
