import numpy as np

def grid_copy(grid):
    n=len(grid)
    m=len(grid[0])
    new_grid = np.empty(shape=(n, m))
    for i in range(0,n):
        for j in range(0,m):
            new_grid[i,j]=grid[i,j]
    return new_grid

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
        for i in range(0,len(grid[0])):
            grid[i,c]=val
    elif c == 999:
        for i in range(0,len(grid)):
            grid[r,i]=val
    return grid

def side_set(side,val,grid):
    if side == "w":
        c = 1
        r = 999
    elif side == "e":
        c = len(grid[0])-2
        r = 999
    elif side == "n":
        c = 999
        r = 1
    else:
        c = 999
        r = len(grid) - 2

    if c == 999:
        for i in range(2,len(grid[0])-1):
            grid[r,i]=val
    elif r == 999:
        for i in range(1,len(grid)-1):
            grid[i,c]=val


    return grid

def boundary_absorb(val,grid):
    new_grid = boundary_set('w',val,grid)
    new_grid = boundary_set('n', val, new_grid)
    new_grid = boundary_set('e', val, new_grid)
    new_grid = boundary_set('s', val, new_grid)
    return grid

def boundary_reflect(grid):
    m = len(grid)
    n = len(grid[0])
    new_grid = grid_copy(grid)
    for i in range(0, m):
        for j in range(0, n):
            if i == 0 and j == 0:   #This if/elif takes care of the corners
                k = 1
                l = 1
            elif i==0 and j==n-1:
                k = 1
                l = n-2
            elif i == m-1 and j == 0:
                k = m-2
                l = 1
            elif i == m-1 and j == n-1:
                k = m-2
                l = n-2
            else:               #This else takes care of the edges
                if i == 0:
                    k = 1
                    l = j
                elif j == 0:
                    k = i
                    l = 1
                elif i == m-1:
                    k = m-2
                    l = j
                elif j == n-1:
                    k = i
                    l = n-2
                else:
                    k = i
                    l = j
            new_grid[i, j] = new_grid[k,l]
    return new_grid



def boundary_reflect_old(grid):
    rows = len(grid)
    cols = len(grid[0])
    new_grid = grid_copy(grid)
    west = new_grid[1,1]
    east = new_grid[1,cols-2]
    north = new_grid[1,2]
    south = new_grid[rows-2,2]
    for i in range(2, cols-2): #north
        new_grid[0, i] = north
    for i in range(2, cols-2): #south
        new_grid[rows-1, i] = south
    for i in range(0,rows): #west
        new_grid[i,0]=west
    new_grid[0,1]=west
    new_grid[rows-1,1]=west
    for i in range(0,rows): #east
        new_grid[i,cols-1]=east
    new_grid[0,cols-2]=east
    new_grid[rows-1,cols-2]=east

    return new_grid

def boundary_donut(grid):
    #takes an nxn grid and returns an (n+2)x(n+2) grid with toroidal BC's applied
    rows = len(grid)
    cols = len(grid[0])

    new_grid = grid_copy(grid)
    for i in range(0,rows): #west
        new_grid[i,0]=grid[i,cols-2]
    for i in range(0,rows): #east
        new_grid[i,cols-1]=grid[i,1]
    for i in range(0, cols): #north
        new_grid[0, i] = grid[rows-2, i]
    for i in range(0, cols): #south
        new_grid[rows-1, i] = grid[1, i]
    return new_grid
