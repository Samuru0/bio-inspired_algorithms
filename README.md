# Bio-Inspired Algorithms
Course Algoritmos Bioinspirados 2026A

This repository contains Python implementations of three classic bio-inspired optimisation algorithms, each in its own self-contained directory.

---

## Repository Structure

```
bio-inspired_algorithms/
├── genetic_algorithm/
│   ├── ___.py   # GA implementation
│   └── README.md
├── ant_colony_optimization/
│   ├── ____.py   # ACO implementation
│   └── README.md
└── particle_swarm_optimization/
    ├── ________.py   # PSO implementation
    └── README.md
```

---

## Algorithms

### 1. [Simple Genetic Algorithm (SGA)](genetic_algorithm/)
Mimics natural selection to evolve a population of binary-encoded solutions toward an optimal value. Demonstrates **selection**, **crossover**, and **mutation** operators.

**Problem solved:** Maximise f(x) = x²

---

### 2. [Ant Colony Optimization (ACO)](ant_colony_optimization/string_evolution/)
Simulates the pheromone-guided foraging of ants to discover short paths through a graph. Demonstrates **pheromone trails**, **probabilistic path selection**, and **evaporation**.

**Problem solved:** Travelling Salesman Problem (TSP)

---

### 3. [Particle Swarm Optimization (PSO)](particle_swarm_optimization/)
Models the collective movement of a swarm, where each particle balances exploration with attraction to the best known positions. Demonstrates **velocity update**, **inertia**, and **cognitive/social** learning.

**Problem solved:** Minimise the Sphere function f(**x**) = Σ xᵢ²

---

## Requirements

- Python 3.x (no external libraries required — uses only the standard library)

## Running an algorithm

```bash
cd genetic_algorithm
python _______.py

cd ant_colony_optimization
python ________.py

cd particle_swarm_optimization
python _______-.py
```
