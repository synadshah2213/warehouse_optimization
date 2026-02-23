grid = []                    # start with an empty grid

for i in range(10):          # do this 10 times
    row = [0] * 10           # create one row
    grid.append(row)         # add that row to the grid
#Placeing the objects in the grid
grid[0][0] = 3
grid[2][3] = 1
grid[4][5] = 2
grid[6][2] = 2
grid[8][8] = 2
grid[1][1] = -1
grid[3][4] = -1
grid[5][7] = -1
grid[7][3] = -1

for row in grid:
    print(row)
    
item_positions = {"item_A": (4,5), "item_B": (6,2), "item_C": (8,8)}
print(item_positions)

order = ["item_A", "item_C"]
print(order)

for x in order:
    item_positions[x]
    print(item_positions[x])