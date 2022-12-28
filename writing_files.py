#python allows you to work with external files

game_file = open("text.txt", "a") #using a appends onto end, if you use w it will overwrite it

game_file.write("\nDeer, Bear, and Ducks") #will write to actual text file and add to it.

game_file.close()