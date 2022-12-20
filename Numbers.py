from math import * #imports math module that allows access to math functions that we normally don't have access to

print(2) #whole number
print(2.0987) #decimal number
print(-2.0987) #negative number

print(3 + 4.5) #basic addition arithmetic
print(3 - 4.5) #subtraction arithmetic
print( 3 * 4.5) #multipulcation
print(3/4.5) #division

print( 3 * 4 + 5) #python uses order of operations when calculating.

print(3 * (4+5)) #can use parenthesis to specify order of operations

#modulus operator returns the remainder
print(10 % 3) #10 mod 3, takes first number divided by second number and then outputs the remainder.

my_num = 5
print(my_num) #passing integer variable to print statement

print(str(my_num)) #converts the integer into a string (can be used for when printing numbers along with strings)

print(str(my_num) + " is my favorite number") #cannot print number with string. Have to convert it into string first to prevent error.

my_num = -5 #updating the value
print(abs(my_num)) #will output the absolute value of integer

print(pow(3,2)) #power function, essentially same as 3 squared = 9
print(pow(4,6))

print(max(4,6)) #max function will return the highest number between the two
print(min(4,6)) #min function returns the lowest number

print(round(3.2)) #round function rounds number to nearest value (uses standard math rules) #rounds to 3
print(round(3.7)) #rounds to 4

print(floor(3.7)) #will grab lowest number 
print(ceil(3.7)) #will round the number up

print(sqrt(36)) #takes the square root of a number and returns a float