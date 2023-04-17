"""Write a function called your_vat. The function takes no parameter. 
The function asks the user to input the price of an item and VAT (vat should be a percentage). 
The function should return the price of the item plus VAT. If the price is 220 and, 
VAT is 15% your code should return a vat inclusive price of 253. Make sure that your code
can handle ValueError. Ensure the code runs until valid numbers are entered. 
(hint: Your code should include a while loop)."""

def your_VAT():
    inp = True
    while inp:
        price = float(input("price of the item - "))
        vat = float(input("vat percentage - "))
        if price >= 0 and vat >= 0:
            inp = False
            final_price = price + (price / 100) * 15
            return final_price
        
#print("Final price of the item: ", your_VAT())


"""Write a function called Python_snakes that takes a number as an argument and creates the 
following shape,using the number’s range: (hint: Use the loops and emoji library."""

def python_snakes(n):
    for i in range(n):
        print('*' * i)
        
python_snakes(5)