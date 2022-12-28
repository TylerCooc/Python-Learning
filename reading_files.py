#in case you want to read from text html csv files can use python read command

game_file = open("text.txt", "r") 
                          #r stands for read, can only read the file
                          #w stands for write, can change existing data within file
                          #a stands for append, can append info to end of file
                          #r+ read and write can do reading and writing functions
                          #stores the content of the file in that variable


#print(game_file.readable()) #will check if file is readable
#print(game_file.read()) #will print out the contents of the file

#print(game_file.readline()) #reading the first line of the file
print(game_file.readlines()) #can read the files in an array format, can add brackets to index certain lines

game_file.close() #have to close the file when you open it