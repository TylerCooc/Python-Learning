#Functions are a collection of code that do a specific task.
#Create lines of code and put into a function. Then you can call the function when needed.
#def is keyword for function
#parameter is information we give to a function

def say_hi(): #function header
    print("Hello User") #have to indent to be within the function

print("Top")
say_hi() #calls the function. Jumps to the say_hi function and executes the code, then jumps back and moves to the next line.
print("Bottom")

def sayhi(name, age): #functions can take multiple parameters to be passed.
    print("Hello " + name + " you are "+ str(age))

sayhi("Mike", 35) #passing parameters to our function
sayhi("Steve", 60)