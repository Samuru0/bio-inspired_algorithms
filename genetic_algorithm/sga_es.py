import random
import string

# ==============================
# Problem Parameters
# ==============================

TARGET = "HOLA MUNDO"
POPULATION_SIZE = 200 # size  = 20 for testing, leads to an infinite loop of generations and keeps fitness at 2
MUTATION_RATE = 0.01 # rate = 0.01 for testing
ELITE_SIZE = 20 # size = 20 for testing
GENES = string.ascii_uppercase + " "

# ==============================
# GA Components
# ==============================

def create_individual():
    """Create a random string of the same length as TARGET."""
    return ''.join(random.choice(GENES) for _ in range(len(TARGET)))


def fitness(individual):
    """
    Fitness function:
    Counts how many characters match the target string
    at the correct position.
    """
    score = 0
    for i in range(len(TARGET)):
        if individual[i] == TARGET[i]:
            score += 1
    return score


def mutate(individual):
    """
    Mutation operator:
    Each character has a small probability of being replaced
    by a random character from the gene set.
    """
    individual = list(individual)
    for i in range(len(individual)):
        if random.random() < MUTATION_RATE:
            individual[i] = random.choice(GENES)
    return ''.join(individual)


def create_initial_population():
    """Generate the initial population."""
    return [create_individual() for _ in range(POPULATION_SIZE)]


# ==============================
# Main Genetic Algorithm Loop
# ==============================

def genetic_algorithm():
    population = create_initial_population()
    generation = 0

    while True:
        generation += 1

        # Evaluate and sort population by fitness
        population = sorted(population, key=fitness, reverse=True)
        best = population[0]

        print(f"Generation {generation}: {best} | Fitness: {fitness(best)}")

        # Termination condition
        if fitness(best) == len(TARGET):
            print("\nTarget string evolved successfully!")
            break

        # Elitism: keep the best individuals
        next_generation = population[:ELITE_SIZE]

        # Generate rest of the population
        while len(next_generation) < POPULATION_SIZE:
            parent = random.choice(population[:50])
            child = mutate(parent)
            next_generation.append(child)

        population = next_generation


# ==============================
# Run the Algorithm
# ==============================

if __name__ == "__main__":
    genetic_algorithm()
