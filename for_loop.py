
# can name the for variable anything
friends = ["jim", "karen", "kevin"] #array

for letter in "Giraffe Academy": #for every letter in the string will execute code
    print(letter)

for friend in friends: #loops through array
    print(friend)

for index in range(10): #starts from 0 and goes to 9
    print(index)

for index in range(3,10):
    print(index)

for index in range(len(friends)): #passes the length of friends array  and will print 0 1 2 indexes
    print(friends[index])

for index in range(5):
    if index == 0:
        print("first iteration")
    else:
        print("Not first iteration")