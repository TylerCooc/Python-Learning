print("Giraffe\nAcademy") #\n creates a new line
print("Giraffe\"Academy") #\" prints out a quotation mark
print("Giraffe\Academy") #prints our a normal back slash

phrase = "Giraffe Academy" #setting string variable to a message
print(phrase)   #passes phrase (string variable) into print statement to print message

print(phrase + " is cool") #concatenating a string to another string. Concenation is connecting two strings together

print(phrase.lower()) #converts string to lowercase
print(phrase.upper()) #converts string to uppercase

print(phrase.isupper()) #checks if variable is uppercase and returns proper boolean value
print(phrase.islower()) #checks if variable is lowercase and returns proper boolean value

print(phrase.upper().isupper()) #converts the string to uppercase and then checks if it actually is uppercase

print(len(phrase)) #passes phrase to length function to check characters in the string

print(phrase[0]) #specifies the index of the string to print a character (strings start from index 0)
print(phrase[3]) #specified the 4th character in the string (0123)

print(phrase.index("G")) #giving index a value, this is passing a parameter. A value that you give to a function is a parameter. 
print(phrase.index("a")) 
print(phrase.index("Academy")) #returns where the string starts. 

print(phrase.replace("Giraffe", "Elephant")) #will replace the old string with new string. 