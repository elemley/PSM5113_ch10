from math import *
import numpy as np
import matplotlib.pyplot as plt
from psm_plot import *
from random import *

def boundary_set(side,val,grid):
    if side == "w":
        c = 0
        r = 999
    elif side == "e":
        c = len(grid[0])-1
        r = 999
    elif side == "n":
        c = 999
        r = 0
    else:
        c = 999
        r = len(grid) - 1

    if r == 999:
        for i in range(0,len(grid)):
            grid[i,c]=val
    elif c == 999:
        for i in range(0,len(grid[0])):
            grid[r,i]=val
    return grid

def boundary_absorb(val,grid):
    new_grid = boundary_set('w',val,grid)
    new_grid = boundary_set('n', val, new_grid)
    new_grid = boundary_set('e', val, new_grid)
    new_grid = boundary_set('s', val, new_grid)
    return grid

def boundary_reflect(grid):
    rows = len(grid)
    cols = len(grid[0])
    new_grid = grid
    for i in range(0,rows): #west
        new_grid[i,0]=grid[i,1]
    for i in range(0,rows): #east
        new_grid[i,cols-1]=grid[i,cols - 2]
    for i in range(0, cols): #north
        new_grid[0, i] = grid[1, i]
    for i in range(0, cols): #south
        new_grid[rows-1, i] = grid[rows-2, i]
    return new_grid

def boundary_donut(grid):
    rows = len(grid)
    cols = len(grid[0])
    new_grid = grid
    for i in range(0,rows): #west
        new_grid[i,0]=grid[i,cols-2]
    for i in range(0,rows): #east
        new_grid[i,cols-1]=grid[i,1]
    for i in range(0, cols): #north
        new_grid[0, i] = grid[rows-2, i]
    for i in range(0, cols): #south
        new_grid[rows-1, i] = grid[1, i]
    return new_grid




#make an array

m = 12  #rows
n = 12  #cols
#m and n include the ghost rows...
hot = 150.0 #temp in degrees C
temp = np.empty(shape=(m,n))

for i in range(0,m):
    for j in range(0,n):
        temp[i,j]=hot

#absorb BC
ambient = 25.0 #deg C
#temp_bc = boundary_absorb(ambient,temp)


#reflect BC
#let's make a few cells on the boundary not the same ...
medium = 75.0
cold = 0.0
really_cold = -10.0
pretty_hot = 100.0
temp[1,1]= really_cold
temp[5,1]=medium
temp[5,10]=cold
temp[10,7]=cold
temp[1,4]=medium
temp[10,10]=really_cold
temp[1,8]=pretty_hot
temp[10,3]=pretty_hot

#temp_bc = boundary_reflect(temp)
temp_bc = boundary_donut(temp)

rectangle = plt.Rectangle((0.5,0.5),m-2,n-2,fc='none')
plt.gca().add_patch(rectangle)
plt.imshow(temp_bc, cmap='hot', interpolation='nearest')
plt.show()















