"""Write a function called user_name, that creates a username for the user. 
The function should ask a user to input their name. The function should then 
reverse the name and attach a randomly issued number between 0 – 9 at the end of the name. 
The function should return the username."""
import random


def user_name():
    name = input("Enter your name ")
    username = name[::-1] + str(random.randint(0, 9))
    return username


# print(user_name())


"""names = [ "Peter", "Jon", "Andrew"]
Write a function called sort_length that takes a list of strings as an argument, 
and sorts the strings in ascending order according to their length.
For example, the list above should return: ['Jon', 'Peter', 'Andrew']"""


def sort_list(lst):
    m = []
    while lst:
        m += [lst.pop(lst.index(min(lst)))]

    return m


print(sort_list(['Jon', 'Peter', 'Andrew']))
