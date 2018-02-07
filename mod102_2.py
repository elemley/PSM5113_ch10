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


#make an array

m = 22  #rows
n = 12  #cols
ambient = 25.0 #temp in degrees C
temp = np.empty(shape=(m,n))

for i in range(0,m):
    for j in range(0,n):
        temp[i,j]=ambient

#set some hot and cold spots
hot = 150   #deg C
cold = 0    #deg C
medium = 75 #deg C

temp_bc = boundary_set('w',hot,temp)

temp_bc = boundary_set('n',medium, temp_bc)
temp_bc = boundary_set('e',cold,temp_bc)



plt.imshow(temp_bc, cmap='hot', interpolation='nearest')
plt.show()















