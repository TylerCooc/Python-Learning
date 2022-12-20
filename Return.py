#python functions are a collection of code that perform a specific tasks.
#using a return statement we can return the information from a python call

def cube(number):
    return number * number * number #python will execute the function and return a value back to the function
                                    #cannot put code below a return statement

result = cube(4) #stores the value being returned from the function

print(result)