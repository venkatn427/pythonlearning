"""Create a function called all_the_same that takes one argument, a string, a list, or a 
tuple and checks if all the elements are the same. If the elements are the same, the function 
should return True. If not, it should return False. For example, [‘Mary’, ‘Mary’, ‘Mary’] 
should return True."""

def all_the_same(ele):
    dct = {}
    for e in ele:
        if e in dct:
            dct[e] += 1
        else:
            dct[e] = 1
            
    return len(dct) == 1

print(all_the_same(['Mary', 'Mary', 'Mary']))

""" str1 = "the love is real"
Write a function called read_backwards that takes a string as an argument and reverses it. 
For example, the string above should return: "real is love the"""

def read_backwards(str1):
    l = str1.split(" ")
    return " ".join(l[::-1])


str1 = "the love is real"
print(read_backwards(str1))

         
     