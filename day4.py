from collections import defaultdict
"""
Write a function called only_floats, which takes two parameters a and b, and returns 2 if both arguments are floats, 
returns 1 if only one argument is a float, and returns 0 if neither argument is a float. If you pass (12.1, 23) 
as an argument, your function should return a 1.
"""


def only_floats(a, b):
    if isinstance(a, float) and isinstance(b, float):
        return 2
    elif isinstance(a, float) or isinstance(b, float):
        return 1
    else:
        return 0


#print(only_floats(12.1, 23))

"""Write a function called word_index that takes one argument, 
a list of strings and returns the index of the longest word in 
the list. If there is no longest word (if all the strings are 
of the same length), the function should return zero (0). 
For example, the list below should return 2.
"""

def word_index(words):
    max_len = 0
    seen = defaultdict(list)
    for i, each in enumerate(words):
        l = len(each)
        if l > max_len:
            max_len = l
            seen[l] = []
        else:
            continue
        seen[l].append(i)
        
    if seen[max(seen)] == len(words):
        return 0

    return seen[max(seen)][0]
        

print(word_index(["Hate", "remorse", "vengeance"]))
print(word_index(["Love", "Hate"]))