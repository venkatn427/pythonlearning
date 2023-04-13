"""Write a function called hide_password that takes no parameters. The function takes an input (a password) from a user and returns a hidden password. For example, if the user enters ‘hello’ as a password the function should return ‘****’ as a password and tell the user that the password is 4 characters long."""

def hide_password():
    s = input('enter the password')
    psw = ''
    psln = len(s) - 1
    newpswd = '*' * psln
    
    return newpswd, psln

# out = hide_password()
# print("password is {} and {} characters long".format(out[0], out[1]))


"""Your new company has a list of figures saved in a list. 
The issue is that these numbers have no separator. 
The numbers are saved in the following format:
[1000000, 2356989, 2354672, 9878098].
You have been asked to write a code that will convert each 
of the numbers in the list into a string. 
Your code should then add a comma on each number as a 
thousand separator for readability. When you run your 
code on the above list, your output should be:
[ '1,000,000', '2,356,989', '2,354,672', '9,878,098’]
Write a function called convert_numbers that will take one 
argument, a list of numbers above."""

def convert_numbers(nums):
    str_out = []
    for num in nums:
        val = f"{int(num):,d}"
        str_out.append(str(val))
        
    return str_out

print(convert_numbers([1000000, 2356989, 2354672, 9878098]))        