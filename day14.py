"""Write a function called flat_list that takes one argument, a nested list. 
The function converts the nested list into a one-dimension list.
For example [[2,4,5,6]] should return [2,4,5,6]."""


def flat_list(nl):
    final_list = []

    def inner_list(il):
        for e in il:
            final_list.append(e)

    for each in nl:
        if type(each) == list:
            inner_list(each)
        else:
            final_list.append(each)
    return final_list


print(flat_list([1, [2, 4, 5]]))

"""A school has asked you to write a program that will calculate teachers' salaries. 
The program should ask the user to enter the teacher’s name, the number of periods 
taught in a month, and the rate per period. The monthly salary is calculated by multiplying 
the number of periods by the monthly rate. The current monthly rate per period is $20. 
If a teacher has more than 100 periods in a month, everything above 100 is overtime. 
Overtime is $25 per period. 
For example, if a teacher has taught 105 periods, their monthly gross salary should be 2,125. 
Write a function called your_salary that calculates a teacher’s gross salary. 
The function should return the teacher’s name, periods taught, and gross salary. 
Here is how you should format your output:
Teacher: John Kelly, Periods: 105
Gross salary:2,125"""


def cal_salary():
    name = input("Enter the teacher name ")
    periods = int(input("Number of periods "))
    # rpp = int(input("Rate per period"))
    grosssal = 0
    if periods > 100:
        regsal = 100 * 20
        extrasal = (periods - 100) * 25
        grosssal = regsal + extrasal
    if periods < 100:
        grosssal = periods * 20

    return name, grosssal, periods


out = cal_salary()

print("Teacher: {} \nPeriods : {} \nGross Salary: {}".format(out[0], out[2], out[1]))
