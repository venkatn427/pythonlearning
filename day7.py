"""Write a function called string_range that takes a single number and returns a string of its range. The string characters should be separated by dots(.) For example, if you pass 6 as an argument, your function should return ‘0.1.2.3.4.5’."""

def string_range(n):
    nstr = ""
    for i in range(n):
        if len(nstr) > 0:
            nstr = nstr + "." + str(i)
        else:
            nstr = str(i)
    return nstr

print(string_range(6))  


"""You are given a list of names, and you are asked to write a code that returns all the names that start with ‘S’. Your code should return a dictionary of all the names that start with S and how many times they appear in the dictionary. Here is a list below:"""  

names = ["Joseph","Nathan", "Sasha", "Kelly", "Muhammad", "Jabulani", "Sera", "Patel", "Sera"]

def dict_of_names(lst):
    n = {}
    for name in lst:
        if name.lower().startswith('s'):
            if name not in n:
                n[name] = 1 
            else:
                n[name] += 1
            
    return n

print(dict_of_names(names))