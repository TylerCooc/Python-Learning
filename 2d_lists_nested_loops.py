
grid =[1,2,3,4] #regular lists

number_grid=[
    [1,2,3],
    [4,5,6],            #number grid list has 4 list elements with 4 rows and 3 columns
    [7,8,9],
    [0]
] 

print(number_grid[0][2]) #will print 3 since it is targeting row 0 and 3rd column

print(number_grid[0])#will print the row

for row in number_grid: #will print all the row elements in the list
    print(row)

for row in number_grid: #will print all the numbers in the grid
    for col in row:
        print(col)