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
v
#num = diffusion(diff_rate,8,10,temp)

#temp = reflectingLat(temp)

print temp
#rectangle = plt.Rectangle((0.5,0.5),n-2,m-2,fc='none')
#plt.gca().add_patch(rectangle)

cmap1 = LinearSegmentedColormap.from_list("my_map",((0,0,1),(1,0,0)),10)
plt.imshow(temp, cmap=cmap1, interpolation='nearest')

#plt.imshow(temp, cmap='hot', interpolation='nearest')
plt.show()


