"""Write a function called same_in_reverse that takes a string and checks if the string reads 
the same in reverse. If it is the same, the code should return True if not, it should return False.
For example, ‘dad’ should return True, because it reads the same in reverse."""


def same_in_reverse(stt):
    return stt == stt[::-1]


print(same_in_reverse('dad'))


def isPalindrome(string):
    found = True
    for i in range((len(string) + 1) // 2):
        if string[i] != string[len(string) - 1 - i]:
            found = False
            break
    return found


print(isPalindrome('teset'))

"""Write a function called your_age. This function asks a student to enter their name and then it 
returns their age. For example, if a user enters Peter as their name, your function should return,
‘Hi, Peter, you are 27 years old. This function reads data from the database (dictionary below).
If the name is not in the dictionary, your code should tell the user that their name is not in 
the dictionary, and ask them for their age. Your code should then add the name and age to the 
dictionary of names_age below. Once added your code should return to the user ‘Hi, (added name), 
you are (added age) years old’. Remember to convert the input from user to lowercase letters"""


def yourage(your_name):
    names_age = {"jane": 23, "kerry": 45, "tim": 34, "peter": 27}
    for name, age in names_age.items():
        if name.lower() == your_name.lower():
            return "Hi, {}, you are {} years old".format(your_name, age)


print(yourage('Jane'))
