lucky_numbers = [4, 8, 15, 16, 23, 42]

friends = ["Kevin", "Karen", "Jim","Oscar", "Toby"]

print(friends) #prints out the friends list

#friends.extend(lucky_numbers) #extends the list to combine both together.
print(friends)

friends.append("Creed") #adds another element to end of the list
print(friends)

friends.insert(1, "Kelly") #will add new element to index location and pushes rest of indexes 1 to the right
print(friends)

friends.remove("Jim") #able to target elements and remove them
print(friends)

friends.pop() #removes an element off the list (in this case the last one)
print(friends)

print(friends.index("Kevin"))# returns the index of an element in the list

print(friends.count("Toby")) #counts the number of targeted element

friends.sort() #sorts the lists in alphebetical order
print(friends)

lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse() #reverse the order of the list
print(lucky_numbers)

friends2 = friends.copy() #can copy the attributes of another list into another. IN this case from previous friends list to another one.
print(friends2)

friends.clear() #returns an empty list, by removing all elements

