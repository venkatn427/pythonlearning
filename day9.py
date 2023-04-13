"""Create a function called biggest_odd that takes a string of numbers and returns the biggest odd number in the list. For example, if you pass ‘23569’ as an argument, your function should return 9. Use list comprehension."""

def biggest_odd(s):
    o = []
    for each in s:
        n = int(each)
        if n % 3 == 0:
            o.append(n)
        
    return max(o)

print(biggest_odd('23569'))

"""Write a function called zeros_last. This function takes a list as argument. If a list has zeros (0), it will move them to the front of the list and maintain the order of the other numbers in the list. If there are no Zeros in the list, the function should return the original list sorted in ascending order. 
For example, if you pass [1, 4, 6, 0, 7,0,9] as an argument, your code should return [1, 4, 6, 7, 9, 0, 0]. 
If you pass [2, 1, 4, 7, 6] as your argument, your code should return [1, 2, 4, 6, 7]."""

def zeros_last(l):
    l1 = []
    allz = []
    for each in l:
        if 0 in l:
            if each == 0:
                allz.append(each)
            else:
                l1.append(each)
        else:
            return sorted(l)
                       
    return l1 + allz
    
l = [1, 4, 6, 0, 7,0,9]
l2 = [2,1,4,7,6]

print(zeros_last(l))
print(zeros_last(l2))