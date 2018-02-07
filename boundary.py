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
    rows = len(grid)
    cols = len(grid[0])
    new_grid = grid
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
