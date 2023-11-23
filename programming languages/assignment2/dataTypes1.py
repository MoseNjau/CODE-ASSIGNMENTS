# MOSES MUIRURI NJAU
# SCT211-0002/2022

import datetime

name = input('Please enter your name: ')
year_of_birth = int(input("Enter your year of birth: "))
print()
print("Hello", name.upper())
print()
current_date = datetime.date.today()

age_years = current_date.year - year_of_birth

birthdate_this_year = datetime.date(current_date.year, 1, 1)

age_days = (current_date - birthdate_this_year).days

age_months = age_days // 30
age_days %= 30

print(f"Your age is: {age_years} years, {age_months} months, and {age_days} days.")
print()
operators = {'A': 'Addition', 'B': 'Subtraction', 'C': 'Multiplication', 'D': 'Division'}
print("Below are the operations")
for i in operators:
    print(i, ":", operators[i])
print()
try:
    operator = input("Enter a choice of operation (A, B, C, or D): ")
    num1 = int(input("Enter your 1st number: "))
    num2 = int(input("Enter your 2nd number: "))
    
    if operator.upper() == 'A':
        print(f"The sum of {num1} and {num2} is {num1 + num2}")
    elif operator.upper() == 'B':
        print(f"The difference between {num1} and {num2} is {abs(num1 - num2)}")  
    elif operator.upper() == 'C':
        print(f"The product of {num1} and {num2} is {num1 * num2}")
    elif operator.upper() == 'D':
        if num2 != 0:
            print(f"The division of {num1} by {num2} is {num1 / num2}") 
        else:
            print("Cannot divide by zero.")
    else:
        print("Input a valid operation (A, B, C, or D)")
except ValueError:
    print("Enter valid numeric inputs.")
except Exception as error:
    print(f"Oops, an Error occurred: {str(error)}")
