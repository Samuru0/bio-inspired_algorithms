"""
Genetic Algorithm (GA)
======================
A bio-inspired search heuristic that mimics the process of natural selection.
This implementation solves a maximization problem using binary-encoded
chromosomes.

Problem: Maximize f(x) = x^2 where x is a non-negative integer encoded in
         binary with a configurable number of bits.
"""

import random


# ─── Parameters ──────────────────────────────────────────────────────────────
POPULATION_SIZE = 10
NUM_BITS = 5          # chromosome length (x ranges from 0 to 2^NUM_BITS - 1)
NUM_GENERATIONS = 20
CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.01
RANDOM_SEED = 42
# ─────────────────────────────────────────────────────────────────────────────


def fitness(chromosome):
    """Decode a binary chromosome to an integer and compute x^2."""
    x = int("".join(str(g) for g in chromosome), 2)
    return x ** 2


def generate_individual():
    """Create a random binary chromosome."""
    return [random.randint(0, 1) for _ in range(NUM_BITS)]


def generate_population(size):
    """Create an initial population of random individuals."""
    return [generate_individual() for _ in range(size)]


def select_parent(population):
    """
    Roulette-wheel (fitness-proportionate) selection.
    Returns one individual selected with probability proportional to fitness.
    """
    fitnesses = [fitness(ind) for ind in population]
    total = sum(fitnesses)
    if total == 0:
        return random.choice(population)
    pick = random.uniform(0, total)
    cumulative = 0
    for ind, f in zip(population, fitnesses):
        cumulative += f
        if cumulative >= pick:
            return ind
    return population[-1]


def crossover(parent1, parent2):
    """Single-point crossover. Returns two offspring."""
    if random.random() < CROSSOVER_RATE:
        point = random.randint(1, NUM_BITS - 1)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        return child1, child2
    return parent1[:], parent2[:]


def mutate(individual):
    """Flip each gene with probability MUTATION_RATE."""
    return [gene ^ 1 if random.random() < MUTATION_RATE else gene
            for gene in individual]


def evolve(population):
    """Produce the next generation through selection, crossover, and mutation."""
    new_population = []
    while len(new_population) < POPULATION_SIZE:
        parent1 = select_parent(population)
        parent2 = select_parent(population)
        child1, child2 = crossover(parent1, parent2)
        new_population.append(mutate(child1))
        new_population.append(mutate(child2))
    return new_population[:POPULATION_SIZE]


def run():
    random.seed(RANDOM_SEED)
    population = generate_population(POPULATION_SIZE)

    print("=" * 45)
    print("       Genetic Algorithm — f(x) = x²")
    print("=" * 45)

    for generation in range(1, NUM_GENERATIONS + 1):
        population = evolve(population)
        best = max(population, key=fitness)
        best_x = int("".join(str(g) for g in best), 2)
        print(f"Generation {generation:>2} | Best x = {best_x:>2} "
              f"| f(x) = {fitness(best):>4} | "
              f"Chromosome: {''.join(str(g) for g in best)}")

    best = max(population, key=fitness)
    best_x = int("".join(str(g) for g in best), 2)
    print("=" * 45)
    print(f"Best solution found: x = {best_x}, f(x) = {fitness(best)}")
    print("=" * 45)


if __name__ == "__main__":
    run()
