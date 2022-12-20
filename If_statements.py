#if statements are a structure in Python, that helps programs make decisions
#can execute certain code when certain conditions are true.

is_male = True
is_tall = False

if is_male:                 #only acts if the condition is true. If is_male changes to false it won't print.
    print("You are a male")
else:                       #if the condition is not true, will execute these lines of code instead.
    print("You are not a male") 

if is_male or is_tall:      #checks if either conditions or true. If neither are true then executes the else
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")

if is_male and is_tall:
    print("You are both male and tall")
else:
    print("You are either not tall or male or both")

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):       #not is a logic function that negates a boolean
    print("You are a short male")
elif not(is_male) and is_tall: #elif is and else if function
    print("you are not a male but are tall")
else:
    print("you are either not male or not tall or both")