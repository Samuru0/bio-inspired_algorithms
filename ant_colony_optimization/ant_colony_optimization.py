import random

# ===============================
# Problem for ants to solve
# ===============================


distances = [ # environment for ants to explore
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
]

num_cities = len(distances) # = size of the problem

# ===============================
# Parameters
# ===============================

num_ants = 10
num_iterations = 50
alpha = 1      # influence of pheromone
beta = 2       # influence of distance
# influence on how ant choose the next path
evaporation = 0.5
pheromone_deposit = 1

# initialize pheromone matrix (initially explore randomly)
pheromone = [[1 for _ in range(num_cities)] for _ in range(num_cities)] 
#stores pheromone levels between cities

# ===============================
# Helper functions
# ===============================

def route_length(route): #total distance of a route | How good is the route?
    length = 0
    for i in range(len(route) - 1):
        length += distances[route[i]][route[i+1]]
    return length


def choose_next_city(current_city, visited): #tow factors: pheromone and distance
    probabilities = []
    total = 0

    for city in range(num_cities):
        if city not in visited:
            tau = pheromone[current_city][city] ** alpha
            eta = (1 / distances[current_city][city]) ** beta
            value = tau * eta
            probabilities.append((city, value))
            total += value

    r = random.random() * total
    cumulative = 0

    for city, prob in probabilities:
        cumulative += prob
        if cumulative >= r:
            return city


# ===============================
# Main
# ===============================

best_route = None
best_length = float("inf")

for iteration in range(num_iterations):

    all_routes = []

    for ant in range(num_ants):

        start = random.randint(0, num_cities - 1) # random ant starting point | like dynamic island model
        route = [start]

        while len(route) < num_cities:
            next_city = choose_next_city(route[-1], route)
            route.append(next_city)

        length = route_length(route)
        all_routes.append((route, length))

        if length < best_length:
            best_length = length
            best_route = route

    # pheromone evaporation
    for i in range(num_cities):
        for j in range(num_cities):
            pheromone[i][j] *= (1 - evaporation) # to avoid pheromone accumulation/convergence

    # pheromone update
    for route, length in all_routes:
        for i in range(len(route) - 1):
            a = route[i]
            b = route[i+1]
            pheromone[a][b] += pheromone_deposit / length # deposit pheromone on the path
            # shorter routes = more pheromone reinforcement

    print(f"Iteration {iteration+1}: Best length = {best_length}")

print("\nBest route found:", best_route)
print("Route length:", best_length)
