"""
Particle Swarm Optimization (PSO)
===================================
A computational method inspired by the social behaviour of bird flocking
or fish schooling. Each particle explores the search space and shares
information about the best positions found.

Problem: Minimize the Sphere function f(x) = sum(xi^2), whose global
         minimum is 0 at the origin.
"""

import random
import math


# ─── Parameters ──────────────────────────────────────────────────────────────
NUM_PARTICLES = 20
NUM_DIMENSIONS = 3
NUM_ITERATIONS = 50
BOUNDS = (-5.12, 5.12)   # search space bounds per dimension
W = 0.5                  # inertia weight
C1 = 1.5                 # cognitive (personal best) coefficient
C2 = 1.5                 # social (global best) coefficient
RANDOM_SEED = 42
# ─────────────────────────────────────────────────────────────────────────────


def sphere(position):
    """Sphere function: sum of squares. Global minimum = 0 at origin."""
    return sum(x ** 2 for x in position)


def random_position():
    """Random position within bounds."""
    lo, hi = BOUNDS
    return [random.uniform(lo, hi) for _ in range(NUM_DIMENSIONS)]


def random_velocity():
    """Random initial velocity (fraction of the search space width)."""
    lo, hi = BOUNDS
    span = hi - lo
    return [random.uniform(-span, span) for _ in range(NUM_DIMENSIONS)]


def clip(value, lo, hi):
    """Clamp a value to [lo, hi]."""
    return max(lo, min(hi, value))


class Particle:
    """Represents one particle in the swarm."""

    def __init__(self):
        self.position = random_position()
        self.velocity = random_velocity()
        self.best_position = self.position[:]
        self.best_fitness = sphere(self.position)

    def update_velocity(self, global_best_position):
        """Update velocity using the PSO velocity equation."""
        r1 = [random.random() for _ in range(NUM_DIMENSIONS)]
        r2 = [random.random() for _ in range(NUM_DIMENSIONS)]
        for d in range(NUM_DIMENSIONS):
            cognitive = C1 * r1[d] * (self.best_position[d] - self.position[d])
            social = C2 * r2[d] * (global_best_position[d] - self.position[d])
            self.velocity[d] = W * self.velocity[d] + cognitive + social

    def update_position(self):
        """Move particle and enforce boundary constraints."""
        lo, hi = BOUNDS
        for d in range(NUM_DIMENSIONS):
            self.position[d] = clip(self.position[d] + self.velocity[d], lo, hi)

    def evaluate(self):
        """Evaluate fitness and update personal best if improved."""
        current_fitness = sphere(self.position)
        if current_fitness < self.best_fitness:
            self.best_fitness = current_fitness
            self.best_position = self.position[:]


def run():
    random.seed(RANDOM_SEED)

    # Initialise swarm
    swarm = [Particle() for _ in range(NUM_PARTICLES)]

    # Identify initial global best
    global_best = min(swarm, key=lambda p: p.best_fitness)
    global_best_position = global_best.best_position[:]
    global_best_fitness = global_best.best_fitness

    print("=" * 55)
    print("   Particle Swarm Optimization — Sphere Function")
    print("=" * 55)

    for iteration in range(1, NUM_ITERATIONS + 1):
        for particle in swarm:
            particle.update_velocity(global_best_position)
            particle.update_position()
            particle.evaluate()

            if particle.best_fitness < global_best_fitness:
                global_best_fitness = particle.best_fitness
                global_best_position = particle.best_position[:]

        pos_str = ", ".join(f"{v:.4f}" for v in global_best_position)
        print(f"Iteration {iteration:>3} | Best fitness: "
              f"{global_best_fitness:.6f} | Position: [{pos_str}]")

    print("=" * 55)
    pos_str = ", ".join(f"{v:.6f}" for v in global_best_position)
    print(f"Best solution found:")
    print(f"  Position: [{pos_str}]")
    print(f"  f(x)    : {global_best_fitness:.6f}")
    print("=" * 55)


if __name__ == "__main__":
    run()
