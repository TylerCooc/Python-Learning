#improved version of our simple calculator
#this calculator will perform all basic arithmetic operations
#will take user input and user arithmetic choice to perform operations

num1 = float(input("Enter first number:")) #takes user input and converts string input into a float
operator = input("Enter operator:")
num2 = float(input("Enter third number:"))

if operator == "+":
    print(num1 + num2)
elif operator == "-":       
    print(num1 - num2)
elif operator == "/":
    print(num1 / num2)      #uses if statements and equal comparator to determine user inteded function
elif operator == "*":
    print(num1 * num2)
else:
    print("Invalid operator")