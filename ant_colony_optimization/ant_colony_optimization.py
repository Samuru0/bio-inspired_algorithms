"""
Ant Colony Optimization (ACO)
==============================
A probabilistic technique inspired by the foraging behaviour of ants.
This implementation solves the Travelling Salesman Problem (TSP) by
building pheromone trails that guide ants toward shorter routes.

Problem: Find the shortest tour that visits every city exactly once
         and returns to the starting city.
"""

import random
import math


# ─── Parameters ──────────────────────────────────────────────────────────────
NUM_ANTS = 10
NUM_ITERATIONS = 50
ALPHA = 1.0          # pheromone importance
BETA = 2.0           # heuristic (distance) importance
EVAPORATION = 0.5    # pheromone evaporation rate
Q = 100              # pheromone deposit constant
RANDOM_SEED = 42
# ─────────────────────────────────────────────────────────────────────────────

# City coordinates (x, y)
CITIES = {
    0: (0, 0),
    1: (2, 4),
    2: (5, 2),
    3: (7, 5),
    4: (3, 7),
    5: (6, 0),
}
NUM_CITIES = len(CITIES)


def euclidean(city_a, city_b):
    """Euclidean distance between two cities."""
    xa, ya = CITIES[city_a]
    xb, yb = CITIES[city_b]
    return math.sqrt((xa - xb) ** 2 + (ya - yb) ** 2)


def build_distance_matrix():
    """Pre-compute all pairwise distances."""
    dist = {}
    for i in range(NUM_CITIES):
        for j in range(NUM_CITIES):
            dist[(i, j)] = euclidean(i, j) if i != j else 0.0
    return dist


def initialise_pheromones():
    """Start all pheromone levels at 1.0."""
    return {(i, j): 1.0
            for i in range(NUM_CITIES)
            for j in range(NUM_CITIES) if i != j}


def tour_length(tour, distance):
    """Total distance of a circular tour."""
    return sum(distance[(tour[i], tour[(i + 1) % NUM_CITIES])]
               for i in range(NUM_CITIES))


def ant_tour(pheromones, distance):
    """
    Build a complete tour for one ant using pheromone-guided probabilistic
    next-city selection.
    """
    start = random.randint(0, NUM_CITIES - 1)
    visited = [start]
    while len(visited) < NUM_CITIES:
        current = visited[-1]
        unvisited = [c for c in range(NUM_CITIES) if c not in visited]
        # Calculate transition probabilities
        desirability = {
            c: (pheromones[(current, c)] ** ALPHA) *
               ((1.0 / distance[(current, c)]) ** BETA)
            for c in unvisited
        }
        total = sum(desirability.values())
        probabilities = {c: desirability[c] / total for c in unvisited}
        # Roulette-wheel selection
        r = random.random()
        cumulative = 0.0
        for city, prob in probabilities.items():
            cumulative += prob
            if r <= cumulative:
                visited.append(city)
                break
        else:
            visited.append(unvisited[-1])
    return visited


def update_pheromones(pheromones, ant_tours, distance):
    """Evaporate existing pheromones and deposit new ones based on tour quality."""
    # Evaporation
    for key in pheromones:
        pheromones[key] *= (1 - EVAPORATION)
    # Deposit
    for tour in ant_tours:
        length = tour_length(tour, distance)
        deposit = Q / length
        for i in range(NUM_CITIES):
            a, b = tour[i], tour[(i + 1) % NUM_CITIES]
            pheromones[(a, b)] += deposit
            pheromones[(b, a)] += deposit


def run():
    random.seed(RANDOM_SEED)
    distance = build_distance_matrix()
    pheromones = initialise_pheromones()

    best_tour = None
    best_length = float("inf")

    print("=" * 55)
    print("   Ant Colony Optimization — Travelling Salesman Problem")
    print("=" * 55)

    for iteration in range(1, NUM_ITERATIONS + 1):
        tours = [ant_tour(pheromones, distance) for _ in range(NUM_ANTS)]
        update_pheromones(pheromones, tours, distance)

        # Track the best tour found so far
        for tour in tours:
            length = tour_length(tour, distance)
            if length < best_length:
                best_length = length
                best_tour = tour[:]

        print(f"Iteration {iteration:>3} | Best tour length so far: "
              f"{best_length:.4f}")

    print("=" * 55)
    print(f"Best tour found: {best_tour}")
    print(f"Tour length:     {best_length:.4f}")
    print("=" * 55)


if __name__ == "__main__":
    run()
