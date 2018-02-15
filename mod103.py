from math import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from psm_plot import *
from boundary import *
from random import *

EMPTY = 0
TREE = 1
BURNING = 2

def initForest(n,probTree,probBurning):
    forest = np.empty(shape=(n,n))
    for i in range(0,n):
        for j in range(0,n):
            rand_tree = random()
            rand_burning = random()
            if rand_tree < probTree:
                if rand_burning < probBurning:
                    forest[i, j] = BURNING
                else:
                    forest[i, j] = TREE
            else:
                forest[i, j] = EMPTY
    return forest

def spread(site,N,E,S,W):
    if (site==EMPTY) or (site==BURNING):
        tmp = EMPTY
    elif (site==TREE) and ((N==BURNING) or (E==BURNING) or (S==BURNING)or (W==BURNING)):
        if random() < probImmune:
            tmp = TREE
        else:
            tmp = BURNING
    elif (site==TREE):
        if (random() < probLightning*(1-probImmune)):
            tmp = BURNING
        else:
            tmp = TREE
    else:
        tmp = TREE
    return tmp

def applyExtended(grid):
    new_grid = grid
    n = len(new_grid)
    for i in range(1,n-1):
        for j in range(1,n-1):
            site = grid[i,j]
            N = grid[i-1,j]
            E = grid[i,j+1]
            S = grid[i+1,j]
            W = grid[i,j-1]
            new_grid = spread(site,N,E,S,W)
    return new_grid


t = 10
n = 50
probTree = 0.8
probBurning = 0.05
probImmune = 0.10
probLightning = 0.001

forest = initForest(n, probTree, probBurning)
forestExtended = boundary_donut(forest)
grids = []
grids.append(forestExtended)

for i in range(0, t):
    forestExtended = boundary_donut(forest)
    forestExtended = applyExtended(forestExtended)
    grids.append(forestExtended)

# print forest

rectangle = plt.Rectangle((0.5, 0.5), n-2, n-2, fc='none')
plt.gca().add_patch(rectangle)

cmap1 = LinearSegmentedColormap.from_list("my_map", ((0, 0, 0), (0, 1, 0), (1, 0, 0)), 3)

print grids[t-1]


for i in range(0, t):
    plt.imshow(grids[i], cmap=cmap1, interpolation='nearest')
    plt.show()





