import itertools
import random
import matplotlib.pyplot as plt

worker = (2,3)
dispatch = (0,0)

def setup_grid():
    """Creates and returns a 15x15 warehouse grid"""
    grid = []
    for i in range(15):
        row = [0] * 15
        grid.append(row)
    grid[0][0] = 3
    grid[2][3] = 1
    grid[4][5] = 2
    grid[6][2] = 2
    grid[8][8] = 2
    grid[10][12] = 2
    grid[12][4] = 2
    grid[14][9] = 2
    grid[3][7] = 2
    grid[7][11] = 2
    grid[1][1] = -1
    grid[3][4] = -1
    grid[5][7] = -1
    grid[7][3] = -1
    grid[9][6] = -1
    grid[11][10] = -1
    return grid

grid = setup_grid()
    
item_positions = {
    "item_A": (4,5),
    "item_B": (6,2),
    "item_C": (8,8),
    "item_D": (10,12),
    "item_E": (12,4),
    "item_F": (14,9),
    "item_G": (3,7),
    "item_H": (7,11)
}

order = ["item_A", "item_B", "item_C", "item_D", "item_E", "item_F", "item_G", "item_H"]
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


def find_optimized_route(order):
    """Finds the optimized route for any number of items"""
    all_distances = []
    for x in list(itertools.permutations(order)):
        total_distance = calculate_distance(worker, item_positions[x[0]])
        for i in range(len(x) - 1):
            total_distance += calculate_distance(item_positions[x[i]], item_positions[x[i+1]])
        total_distance += calculate_distance(item_positions[x[-1]], dispatch)
        all_distances.append(total_distance)
    return min(all_distances)






def run_simulation(order, optimized_distance):    #Runs the simulation 10 times for improved accuracy
    random_distances = []
    optimized_distances = []
    improvements = []
    
    for i in range(10):
        random.shuffle(order)
        random_distance = calculate_distance(worker, item_positions[order[0]])
        for i in range(len(order) - 1):
            random_distance += calculate_distance(item_positions[order[i]], item_positions[order[i+1]])
        random_distance += calculate_distance(item_positions[order[-1]], dispatch)
        improvement = ((random_distance - optimized_distance)/random_distance) * 100
        random_distances.append(random_distance)
        improvements.append(improvement)
        optimized_distances.append(optimized_distance)
    
    return random_distances, optimized_distances, improvements




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

