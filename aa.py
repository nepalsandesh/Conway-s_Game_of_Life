# This module is not used on main.py
# This is just for checking either "get_neighbours()" function works correctly or not..

import numpy
import random

rows = 3
columns = 3

grid_array = numpy.ndarray(shape=(rows, columns))

for x in range(rows):
    for y in range(columns):
        grid_array[x][y] = random.randint(0,1)



print(grid_array)




def get_neighbours(x, y):
    total = 0
    for n in range(-1, 2):
        for m in range(-1,2):
            x_edge = (x+n+rows)%rows
            y_edge = (y+m+columns)%columns
            total += grid_array[x_edge][y_edge]
            print("n = {}, m = {}, x_edge ={}, y_edge={}, total={}".format(n, m, x_edge, y_edge, total))
    total -= grid_array[x][y]
    print("Total = ", total)

    
x = int(input("Enter row index: "))
y = int(input("Enter column index: "))
     
get_neighbours(x, y)

