#can use try except block which will try code and account for if there is an error



try: #will execute the code to see if code is valid or not
    value = 10/0
    number = int(input("Enter a number ")) #normal enter integer input function
    print(number) #will give an error if you enter text when it wants an integer
except ValueError: 
    print("Invalid Input")
except ZeroDivisionError: #two exception blocks one for invalid input and a division by zero error
    print("Divided by zero")