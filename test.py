"""Guive input string, return an output string such that all the lower case characters shotuld be sorted . 

Test@123Google --> Teeg@123Gloost"""

inp = "Test@123Google"

all_lowers = []
for each in inp:
    if each.islower():
        all_lowers.append(each)
new_list = sorted(all_lowers)
new_str = ""
for char in inp:
    if char.islower():
        pass 
        new_str += new_list[0]
        new_list = new_list[1:]
    else:
        new_str += char
print(new_str)
            
        