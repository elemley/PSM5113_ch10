from math import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from psm_plot import *
from boundary import *
from random import *
from time_step_scrolling import *

EMPTY = 0
TREE = 1
BURNING = 2

def main():
    t = 50
    n = 10
    probBurning = 0.05
    probTree = 0.6
    probImmune = 0.40
    probLightning = 0.00001

    forest = initForest(n, probTree, probBurning)   #forest is nxn
    print forest
    forestExtended = boundary_donut(forest)         #forestExtended is (n+2)x(n+2)
    print forestExtended

    grids = []
    grids.append(forest)    #Each item in grids is (n+2)x(n+2)
    print grids[0]

    for i in range(0, t):
        #forest = setForest(forestExtended)  # set internal cells to current state
        print forest
        old_forestExtended = boundary_donut(forest)  # reset boundaries to donut condition
        print old_forestExtended
        new_forestExtended = applyExtended(old_forestExtended, probLightning, probImmune)
        print new_forestExtended
        forest = setForest(new_forestExtended)

        grids.append(forest)

    print grids[1]

    #rectangle = plt.Rectangle((0.5, 0.5), n - 2, n - 2, fc='none')
    #plt.gca().add_patch(rectangle)
    axes = AxesSequence()
    cmap1 = LinearSegmentedColormap.from_list("my_map", ((0, 0, 0), (0, 1, 0), (1, 0, 0)), 3)
    for i, ax in zip(range(t), axes):
        ax.imshow(grids[i], cmap=cmap1, interpolation='nearest')
        ax.set_title("Time Step "+ str(i))
    axes.show()

"""
    # print forest
    rectangle = plt.Rectangle((0.5, 0.5), n - 2, n - 2, fc='none')
    plt.gca().add_patch(rectangle)

    cmap1 = LinearSegmentedColormap.from_list("my_map", ((0, 0, 0), (0, 1, 0), (1, 0, 0)), 3)

    ax1 = plt.subplot(311)
    plt.imshow(grids[0], cmap=cmap1, interpolation='nearest')

    ax2 = plt.subplot(312, sharex=ax1)
    plt.imshow(grids[1], cmap=cmap1, interpolation='nearest')

    ax3 = plt.subplot(313, sharex=ax1)
    plt.imshow(grids[2], cmap=cmap1, interpolation='nearest')

    plt.show()
"""

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

def spread(site,N,E,S,W,probLightning,probImmune):
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

def applyExtended(grid,probLightning,probImmune):
    new_grid = grid_copy(grid)
    n = len(new_grid)
    for i in range(1,n-1):
        for j in range(1,n-1):
            site = grid[i,j]
            N = grid[i-1,j]
            E = grid[i,j+1]
            S = grid[i+1,j]
            W = grid[i,j-1]
            new_grid[i,j] = spread(site,N,E,S,W,probLightning,probImmune)
    return new_grid

def setForest(grid):
    n = len(grid)
    new_grid = np.empty(shape=(n-2, n-2))
    for i in range(0,n-2):
        for j in range(0,n-2):
            new_grid[i,j]=grid[i+1,j+1]
    return new_grid



"""


#plt.imshow(forestExtended, cmap=cmap1, interpolation='nearest')
#plt.show()


"""

"""
axes = AxesSequence()
for i, ax in zip(range(n), axes):
    ax.imshow(grids[i], cmap=cmap1, interpolation='nearest')
    title_string = 'Time Step '+ str(i)
    ax.set_title(title_string.format(i))
axes.show()

"""
if __name__ == '__main__':
    main()
