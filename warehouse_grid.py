import itertools
import random

random_distances = []
optimized_distances = []
improvements = []

grid = []                    # start with an empty grid

worker = (2,3)
dispatch = (0,0)

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

order = ["item_A", "item_C", "item_B"]
print(order)

for x in order:
    item_positions[x]
    print(item_positions[x])


def calculate_distance(pos1, pos2):
    x = abs(pos1[0] - pos2[0])
    y = abs(pos1[1] - pos2[1])
    distance = x + y
    return distance

x = calculate_distance(worker,(4,5)) + calculate_distance((4,5),(8,8)) + calculate_distance((8,8),dispatch)
print(x)

print(list(itertools.permutations(order)))

all_distances = []
for x in list(itertools.permutations(order)):
    print(x)
    total_distance = calculate_distance(worker,item_positions[x[0]]) + calculate_distance(item_positions[x[0]], item_positions[x[1]]) + calculate_distance(item_positions[x[1]],item_positions[x[2]]) + calculate_distance(item_positions[x[2]], dispatch)
    print(total_distance)
    all_distances.append(total_distance)
    print(min(all_distances))

random.shuffle(order)
print(order)

random_distance = calculate_distance(worker, item_positions[order[0]]) + calculate_distance(item_positions[order[0]], item_positions[order[1]]) + calculate_distance(item_positions[order[1]], item_positions[order[2]]) + calculate_distance(item_positions[order[2]], dispatch)
print(random_distance)

improvement = ((random_distance - min(all_distances))/random_distance) * 100
print(improvement)


for row in grid:
    for cell in row:
        if cell == 0:
            print (".", end=" ")
        elif cell == 1:
            print("W", end=" ")
        elif cell == -1:
            print("#", end=" ")
        elif cell == 2:
            print("I", end=" ")
        elif cell == 3:
            print("D", end=" ")
        else:
            print(".", end=" ")
    print()

for i in range(10):
    random.shuffle(order)
    print(order)
    random_distance = calculate_distance(worker, item_positions[order[0]]) + calculate_distance(item_positions[order[0]], item_positions[order[1]]) + calculate_distance(item_positions[order[1]], item_positions[order[2]]) + calculate_distance(item_positions[order[2]], dispatch)
    print(random_distance)  
    improvement = ((random_distance - min(all_distances))/random_distance) * 100
    print(improvement)
    random_distances.append(random_distance)
    improvements.append(improvement)
    optimized_distances.append(min(all_distances))

print(random_distances)
print(optimized_distances)
print(improvements)