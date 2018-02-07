from math import *
import numpy as np
import matplotlib.pyplot as plt
from psm_plot import *
from boundary import *
from random import *

def get_delta_sum(x,y,grid):
    summ = 0.0
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if i != x and j != y:
                summ+=grid[i,j]
    return summ


#make an array
m = 12 #rows
n = 12  #cols
#it is assumed that there are ghost rows all the way around
#m and n include the ghost rows...
hot = 150.0 #temp in degrees C
temp = np.empty(shape=(m,n))
for i in range(0,m):    #set initial temps
    for j in range(0,n):
        temp[i,j]=hot

#reflect BC
#let's make a few cells on the boundary not the same ... and set BC's
medium = 75.0
cold = 0.0
really_cold = -10.0
pretty_hot = 100.0
new_temp=side_set('n',pretty_hot,temp)
new_temp=side_set('s',really_cold,new_temp)
new_temp=side_set('w',medium,temp)
new_temp=side_set('e',cold,new_temp)

temp_bc = boundary_reflect(new_temp)

t = 0.0
dt = 0.1    #seconds
time_steps = 10
r = 0.125   #this is a diffusion parameter

for k in range(0,time_steps):
    for i in range(1,m-2):
        for j in range(1,n-2):
            delta_sum = get_delta_sum(i,j,temp_bc)
            tmp = (1-8*r)*temp_bc[i,j] + r*delta_sum
            temp_bc[i,j]=tmp
    #temp_bc = boundary_reflect(temp_bc)



rectangle = plt.Rectangle((0.5,0.5),n-2,m-2,fc='none')
plt.gca().add_patch(rectangle)
plt.imshow(temp_bc, cmap='hot', interpolation='nearest')
plt.show()















