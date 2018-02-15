from math import *
import numpy as np
import matplotlib.pyplot as plt
from psm_plot import *
from boundary import *
from random import *
from matplotlib.colors import LinearSegmentedColormap

def initBar(m,n,init_temp,hot, hotSites, cold, coldSites):
    grid = np.empty(shape=(m, n))
    for i in range(0, m):  # set initial temps
        for j in range(0, n):
            grid[i, j] = init_temp
    new_grid = applyHotCold(grid,hot, hotSites,cold, coldSites)
    return new_grid

def applyHotCold(grid,hot, hotSites, cold, coldSites):
    new_grid = grid
    for i in range(0,len(hotSites)):
        new_grid[hotSites[i]]=hot
    for i in range(0, len(coldSites)):
        new_grid[coldSites[i]] = cold
    return new_grid

def diffusion(diff_rate, i,j, grid):
    surroundings_sum = grid[i-1,j-1]+grid[i-1,j]+grid[i-1,j+1]
    surroundings_sum+=grid[i,j-1]+grid[i,j+1]
    surroundings_sum+=grid[i+1,j-1]+grid[i+1,j]+grid[i+1,j+1]
    tmp = (1-8*diff_rate)*grid[i,j]+ diff_rate*surroundings_sum
    return tmp

def reflectingLat(grid):
    m = len(grid)
    n= len(grid[0])
    new_grid = np.empty(shape=(m+2, n+2))
    m = len(new_grid)
    n = len(new_grid[0])
    for i in range(0, m):  # set initial temps
        for j in range(0, n):
            if i == 0 or j == 0 or i==m-1 or j==n-1:
                new_grid[i, j] = 0
            else:
                new_grid[i,j] = grid[i-1,j-1]

    final_grid = boundary_reflect(new_grid)
    #final_grid = new_grid
    return final_grid

def applydiffusionextended(diff_rate, grid):
    #apply diffusion to internal cells only
    m = len(grid)
    n= len(grid[0])
    new_grid = np.empty(shape=(m-2, n-2))
    m = len(new_grid)
    n = len(new_grid[0])
    for i in range(0, m):  # set initial temps
        for j in range(0, n):
            new_grid[i,j]=diffusion(diff_rate,i+1,j+1,grid)
    return new_grid

def diffusionSim(m,n,diff_rate,t):
    hot = 50.0
    cold = 0.0
    ambient = 25.0

    hot_list = [(4, 0), (5, 0), (0, 24)]
    cold_list = [(m - 1, 9), (m - 1, 10)]

    temp = initBar(m, n, ambient, hot, hot_list, cold, cold_list)
    for step in range(0,t):
        new_temp = reflectingLat(temp)
        temp = applydiffusionextended(diff_rate,new_temp)
        temp = applyHotCold(temp,hot,hot_list,cold,cold_list)
    return temp

m = 10
n = 30
t_steps = 10
diff_rate = 0.125

temp = diffusionSim(m,n,diff_rate,t_steps)
#hot = 50.0
#cold = 0.0
#ambient = 25.0

#hot_list = [(4, 0), (5, 0), (0, 24)]
#cold_list = [(m - 1, 9), (m - 1, 10)]

#temp = initBar(m, n, ambient, hot, hot_list, cold, cold_list)

#num = diffusion(diff_rate,8,10,temp)

#temp = reflectingLat(temp)

print temp
#rectangle = plt.Rectangle((0.5,0.5),n-2,m-2,fc='none')
#plt.gca().add_patch(rectangle)

cmap1 = LinearSegmentedColormap.from_list("my_map",((0,0,1),(1,0,0)),256)
plt.imshow(temp, cmap=cmap1, interpolation='nearest')

#plt.imshow(temp, cmap='hot', interpolation='nearest')
plt.show()




"""

def get_delta_sum(x,y,grid):
    summ = 0.0
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if i != x and j != y:
                summ+=grid[i,j]
    return summ

#make an array
m = 28 #rows
n = 28  #cols
#it is assumed that there are ghost rows all the way around
#m and n include the ghost rows...
medium = 75.0
cold = 0.0
really_cold = -10.0
pretty_hot = 100.0
hot = 150.0 #temp in degrees C
temp = np.empty(shape=(m,n))
for i in range(0,m):    #set initial temps
    for j in range(0,n):
        temp[i,j]=medium

#reflect BC
#let's make a few cells on the boundary not the same ... and set BC's
new_temp=side_set('n',cold,temp)
new_temp=side_set('s',cold,new_temp)
new_temp=side_set('w',cold,temp)
new_temp=side_set('e',cold,new_temp)

#make a few cells hot
start_i = int(m/2) - int(m/6)
end_i = int(m/2) + int(m/6)
start_j = int(n/2) - int(n/6)
end_j = int(n/2) + int(n/6)
print start_i, start_j, end_i, end_j
for i in range(start_i,end_i):
    for j in range(start_j,end_j):
        new_temp[i,j] = hot


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
    new_temp = side_set('n', cold, temp)
    new_temp = side_set('s', cold, new_temp)
    new_temp = side_set('w', cold, temp)
    new_temp = side_set('e', cold, new_temp)
    temp_bc = boundary_reflect(temp_bc)

#temp_bc = boundary_reflect(temp_bc)

print temp_bc

rectangle = plt.Rectangle((0.5,0.5),n-2,m-2,fc='none')
plt.gca().add_patch(rectangle)
plt.imshow(temp_bc, cmap='hot', interpolation='nearest')
plt.show()















"""