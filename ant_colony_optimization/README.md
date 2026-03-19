# Ant Colony Optimization (ACO)

A probabilistic technique inspired by the **foraging behaviour of ants**. Ants deposit pheromone trails on good paths; over time, shorter routes accumulate more pheromone and are preferred by subsequent ants, leading the colony toward an optimal solution.

## Problem

Solve the **Travelling Salesman Problem (TSP)**: find the shortest tour that visits every city exactly once and returns to the starting city.

## How it works

| Step | Description |
|------|-------------|
| **Initialisation** | Pheromone levels are set to a uniform value on all edges. |
| **Tour construction** | Each ant builds a complete tour by probabilistically choosing the next city based on pheromone strength and distance (heuristic). |
| **Pheromone update** | Pheromones evaporate on all edges; ants deposit new pheromone proportional to the quality (1 / length) of their tour. |
| **Iteration** | The process repeats; shorter paths accumulate pheromone and become increasingly attractive. |

## Key Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `NUM_ANTS` | 10 | Ants per iteration |
| `NUM_ITERATIONS` | 50 | Number of ACO cycles |
| `ALPHA` | 1.0 | Pheromone importance weight |
| `BETA` | 2.0 | Distance (heuristic) importance weight |
| `EVAPORATION` | 0.5 | Pheromone evaporation rate |
| `Q` | 100 | Pheromone deposit constant |

## How to run

```bash
python ant_colony_optimization.py
```

## Example output

```
=======================================================
   Ant Colony Optimization — Travelling Salesman Problem
=======================================================
Iteration   1 | Best tour length so far: 18.7234
Iteration   2 | Best tour length so far: 17.9801
...
Iteration  50 | Best tour length so far: 16.4253
=======================================================
Best tour found: [0, 1, 4, 3, 2, 5]
Tour length:     16.4253
=======================================================
```
