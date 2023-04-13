"""Write a function called odd_even that has one parameter and takes a list of numbers as an argument. The function returns the difference between the largest even number in the list and the smallest odd number in the list. For example, if you pass [1,2,4,6] as an argument the function should return 6 -1= 5"""

def odd_even(l):
    odd = []
    even = []
    for each in l:
        if each % 2 == 0:
            even.append(each)
        else:
            odd.append(each)
    
    return max(even) - min(odd)
    
print(odd_even([1,2,4,6]))


"""Write a function called prime_numbers. This function asks a user to enter a number (integer) as an argument and returns a list of all the prime numbers within its range. For example, if user enters 10, your code should return [2, 3, 5, 7] as prime numbers."""

def prime_num(n):
    pn = [2]
    for num in range(n):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
                else:
                    pn.append(num)
    return set(pn)

print(prime_num(10))