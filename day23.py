"""Create a simple calculator. The calculator should be able to perform basic math operations, add, subtract, divide
and multiply. The calculator should take input from users. 
The calculator should be able to handle ZeroDivisionError, NameError, and ValueError."""

def calculator():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Choose an operation (+, -, *, /): ")
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2
        else:
            print("Invalid operation")
            return
        
        print(f"{num1} {operation} {num2} = {result}")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except ValueError:
        print("Invalid input")
    except NameError:
        print("Undefined variable")

#calculator()


"""s = "love live and laugh"
Write a function called multiply_words that takes a string as an argument and multiplies the 
length of each word in the string by the length of other words in the string.
For example, the string above should return 240 - love (4) live (4) and (3) laugh (5). 
However, your function should only multiply words will all lowercase letters.
If a word has one upper case letter, it should be ignored. For example, the following string:
s = "Hate war love Peace" should return 12 – war (3) love (4). Hate and Peace will be ignored 
because they have at least one uppercase letter."""

def multiply_words(m_s):
    num = 1
    for each in m_s.split(' '):
        if each.islower():
            wl = len(each)
            num = num * wl
    return num

print(multiply_words('Hate war love Peace'))
    