# Bio-Inspired Algorithms
Course Algoritmos Bioinspirados 2026A

This repository contains Python implementations of three classic bio-inspired optimization algorithms, each in its own self-contained directory.

---

## Repository Structure

```
bio-inspired_algorithms/
├── genetic_algorithm/
│   ├── sga_es.py   # GA implementation
│   └── README.md
├── ant_colony_optimization/
│   ├── ant_colony_optimization.py   # ACO implementation
│   └── README.md
└── particle_swarm_optimization/
    ├── pso.py   # PSO implementation
    └── README.md
```

---

## Algorithms

### 1. [Simple Genetic Algorithm (SGA)](genetic_algorithm/string_evolution)
Mimics natural selection to evolve a population of binary-encoded solutions toward an optimal value. Demonstrates **selection**, **crossover**, and **mutation** operators.

**Problem solved:** Maximise the function

---

### 2. [Ant Colony Optimization (ACO)](ant_colony_optimization/)
Simulates the pheromone-guided foraging of ants to discover short paths through a graph. Demonstrates **pheromone trails**, **probabilistic path selection**, and **evaporation**.

**Problem solved:** Travelling Salesman Problem (TSP)

---

### 3. [Particle Swarm Optimization (PSO)](particle_swarm_optimization/)
Models the collective movement of a swarm, where each particle balances exploration with attraction to the best known positions. Demonstrates **velocity update**, **inertia**, and **cognitive/social** learning.

**Problem solved:** Minimise the function

---

## Requirements

- Python 3.x 

## Running an algorithm

```bash
cd genetic_algorithm
python sga_es.py

cd ant_colony_optimization
python ant_colony_optimization.py

cd particle_swarm_optimization
python pso.py
```
