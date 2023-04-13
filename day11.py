"""Write a function called equal_strings. The function takes two strings as arguments and compares them. If the strings are equal (if they have the same characters and have equal length), it should return True, if they are not, it should return False. For example, ‘love’ and ‘evol’ should return True."""

def equal_strings(s1, s2):
    def get_dict(str1):
        d = {}
        for each in str1:
            if each in d:
                d[each] += 1
            else:
                d[each] = 1
        return d
    sd1 = sorted(get_dict(s1))
    sd2 = sorted(get_dict(s2))
    
    return sd1 == sd2
    
print(equal_strings('love','evl'))
    
"""Write a function called swap_values. This function takes a list of numbers and swaps the first element with the last element. For example, if you pass [2, 4,67, 7] as a parameter, your function should return
[7, 4, 67, 2]."""

def swap_values(lst):
    final = []
    for i in range(len(lst)):
        if i == 0:
            final.append(lst[-1])
        elif i == len(lst):
            final.append(lst[0])
        else:
            final.append(lst[i])
    return final

print(swap_values([7, 4, 67, 2]))