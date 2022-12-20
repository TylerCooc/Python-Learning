number1 = input("Enter a whole number: ") #python by default when taking input it is a string.
number2 = input("Enter another whole number: ") #prompts user to input two numbers
number3 = input("Enter a number with decimal: ")
number4 = input("Enter another number with decimal: ")

result = int(number1) + int(number2) #int() converts whatever value inside the parenthesis into a intger. Integers are only whole numbers

result1 = float(number3) + float(number4) #float() floats allow for decimal numbers

print(result) 
print(result1)