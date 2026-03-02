import itertools
import random
import matplotlib.pyplot as plt

worker = (2,3)
dispatch = (0,0)

def setup_grid():                # Creates and returns a 10x10 warehouse grid with all objects placed.
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
    return grid

grid = setup_grid()

for row in grid:
    print(row)
    
item_positions = {"item_A": (4,5), "item_B": (6,2), "item_C": (8,8)}
print(item_positions)

order = ["item_A", "item_C", "item_B"]
print(order)

for x in order:
    item_positions[x]
    print(item_positions[x])


def calculate_distance(pos1, pos2): # Calculates the distance between objects
    x = abs(pos1[0] - pos2[0])
    y = abs(pos1[1] - pos2[1])
    distance = x + y
    return distance

x = calculate_distance(worker,(4,5)) + calculate_distance((4,5),(8,8)) + calculate_distance((8,8),dispatch)
print(x)

print(list(itertools.permutations(order)))


def find_optimized_route(order):    # Finds the optimized route 
    all_distances = []
    for x in list(itertools.permutations(order)):
        total_distance = calculate_distance(worker, item_positions[x[0]]) + calculate_distance(item_positions[x[0]], item_positions[x[1]]) + calculate_distance(item_positions[x[1]], item_positions[x[2]]) + calculate_distance(item_positions[x[2]], dispatch)
        all_distances.append(total_distance)
    return min(all_distances)

optimized_distance = find_optimized_route(order)

random.shuffle(order)
print(order)

random_distance = calculate_distance(worker, item_positions[order[0]]) + calculate_distance(item_positions[order[0]], item_positions[order[1]]) + calculate_distance(item_positions[order[1]], item_positions[order[2]]) + calculate_distance(item_positions[order[2]], dispatch)
print(random_distance)

improvement = ((random_distance - optimized_distance)/random_distance) * 100
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

def run_simulation(order, optimized_distance):    #Runs the simulation 10 times for improved accuracy
    random_distances = []
    optimized_distances = []
    improvements = []
    
    for i in range(10):
        random.shuffle(order)
        random_distance = calculate_distance(worker, item_positions[order[0]]) + calculate_distance(item_positions[order[0]], item_positions[order[1]]) + calculate_distance(item_positions[order[1]], item_positions[order[2]]) + calculate_distance(item_positions[order[2]], dispatch)
        improvement = ((random_distance - optimized_distance)/random_distance) * 100
        random_distances.append(random_distance)
        improvements.append(improvement)
        optimized_distances.append(optimized_distance)
    
    return random_distances, optimized_distances, improvements

random_distances, optimized_distances, improvements = run_simulation(order, optimized_distance)

avg_random_distances = sum(random_distances)/len(random_distances)
print(avg_random_distances)

avg_optimized_distances = sum(optimized_distances)/len(optimized_distances)
print(avg_optimized_distances)

avg_improvement = sum(improvements)/len(improvements)
print(avg_improvement)

min_improvement = min(improvements)
print(min_improvement)

max_improvement = max(improvements)
print(max_improvement)


def visualize_warehouse():      #function that visualizes the warehouse usign matplotlib 
    fig, ax = plt.subplots()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.grid(True)
    ax.plot(0, 0, marker="s", color="red", markersize=15, label="Dispatch")
    ax.plot(2, 3, marker="o", color="blue", markersize=15, label="Worker")
    ax.plot(5, 4, marker="*", color="green", markersize=15, label="item_A")
    ax.plot(2, 6, marker="*", color="green", markersize=15, label="item_B")
    ax.plot(8, 8, marker="*", color="green", markersize=15, label="item_C")
    ax.plot([2, 5, 2, 8, 0], [3, 4, 6, 8, 0], linestyle="-", color="purple", label="Optimized Route")
    ax.plot([2, 5, 2, 8, 0], [3, 6, 4, 8, 0], linestyle="--", color="orange", label="Random Route")
    ax.legend()
    ax.set_title("Warehouse Layout")

visualize_warehouse()

runs = list(range(10))
fig2, ax2 = plt.subplots()
ax2.bar(runs, random_distances, width=0.4, label="Random Route", color="orange")
ax2.bar([r + 0.4 for r in runs], optimized_distances, width=0.4, label="Optimized Route", color="purple")
ax2.set_xlabel("Simulation Run")
ax2.set_ylabel("Distance")
ax2.set_title("Random vs Optimized Distance")
ax2.legend()
plt.show()