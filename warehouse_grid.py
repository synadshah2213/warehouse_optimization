grid = []                    # start with an empty grid

for i in range(10):          # do this 10 times
    row = [0] * 10           # create one row
    grid.append(row)         # add that row to the grid
#Placeing the objects in the grid
grid[0][3] = 1
grid[6][7] = -1
grid[8][2] = 2
grid[4][9] = 3

for row in grid:
    print(row)
    