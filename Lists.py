#lists is an ordered data structure. uses square brackets. 

friends = ["Kevin", "Karen", "Jim"] #list of friends(strings). Lists have index and start at 0. kevin is 0 and jim is 2.

values = ["Kevin", 2, False] #can put any value inside of a list strings,numbers,booleans...etc. 

print(friends) #can pass a list as a parameter 

print(friends[0]) #targets the 0 index of our friends list. Prints Kevin

print(friends[-1]) #can access lists backwards, index starts at -1. Prints jim.

#to the right index is 0 1 2, to the left index is -3 -2 -1


print(friends[1:]) #grabs element at index 1 and all elements after that

friends = ["Kevin", "Karen", "Jim","Oscar", "Toby"]
print(friends[1:3]) #will grab index 1 and up to 3, but will not print 3

friends[1] = "Mike" #can update the index value, by targeting specific index and changing its value.

print(friends[1])