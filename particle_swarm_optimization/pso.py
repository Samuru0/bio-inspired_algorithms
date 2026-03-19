import random

# ===============================================
# Find "x" that minimizes the function f(x) = x^2
# ===============================================

def objective_function(x):
    return x**2  # minimum at x = 0

# ===============================
# Parameters
# ===============================

num_particles = 20
num_iterations = 50

w = 0.5      # inertia
c1 = 1.5     # cognitive component
c2 = 1.5     # social component

# ===============================
# Particle Initialization
# ===============================

particles = []
velocities = []

for _ in range(num_particles):
    x = random.uniform(-10, 10)
    v = random.uniform(-1, 1)
    particles.append(x)
    velocities.append(v)

# personal best
p_best = particles[:]
p_best_values = [objective_function(x) for x in particles]

# global best
g_best = p_best[p_best_values.index(min(p_best_values))]

# ===============================
# Main PSO Loop
# ===============================

for iteration in range(num_iterations): 

    for i in range(num_particles):

        r1 = random.random()
        r2 = random.random()

        # Core of algorithm
        # Updates velocity based on current move, own best position and global best position
        velocities[i] = (
            w * velocities[i]
            + c1 * r1 * (p_best[i] - particles[i])
            + c2 * r2 * (g_best - particles[i])
        )

        # update position
        particles[i] += velocities[i]

        # evaluate
        value = objective_function(particles[i])

        # update personal best
        # Each particle evaluates its oown 
        if value < p_best_values[i]: # If new position better than personal best, update personal best
            p_best[i] = particles[i]
            p_best_values[i] = value

    # update global best
    g_best = p_best[p_best_values.index(min(p_best_values))] # Updates global best if new solution found

    print(f"Iteration {iteration+1}: Best = {g_best:.4f}")

print("\nBest solution found:", g_best)