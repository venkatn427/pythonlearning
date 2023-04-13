"""
Create a function called my_discount. The function takes no arguments but asks the user to input the 
price and the discount (percentage) of the product. Once the user inputs the price and discount, 
it calculates the price after the discount. The function should return the price after the discount. 
For example, if the user enters 150 as price and 15% as the discount, your function should return 127.5.
"""

def my_discount():
    price = float(input("enter the price"))
    discount = int(input("enter the discount percentage"))
    
    newprice = price - (price * 15) / 100
    
    print(newprice)

# my_discount()

"""You work for a school and your boss wants to know how many female and male students are enrolled in the school. The school has saved the students in a list. Your task is to write a code that will count how many males and females are in the list. Here is a list below:"""

def count_gen(students):
    cnt = {}
    for each in students:
        n = each.lower()
        if n in cnt:
            cnt[n] += 1
        else:
            cnt[n] = 1
    return [(k,v) for k,v in cnt.items()]

students = ['Male', 'Female', 'female', 'male', 'male', 'male', 'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']

print(count_gen(students))