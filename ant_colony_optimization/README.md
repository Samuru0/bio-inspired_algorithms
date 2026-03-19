# Ant Colony Optimization (ACO)

A probabilistic metaheuristic inspired by the **foraging behavior of ants**. Ants communicate indirectly by laying and following **pheromone trails**: good paths accumulate more pheromone and become more likely to be chosen in future iterations.

This implementation is a compact, educational ACO that searches for a **short route visiting all cities exactly once** (a TSP-like *Hamiltonian path* variant).

---

## Problem (in this code)

Given a fixed distance matrix (`distances`) with 4 cities, find a route that:

- starts at a random city
- visits **every city exactly once**
- minimizes the total distance

> Note: this script **does not** add the edge to return to the starting city, so it does **not** build a closed tour/cycle.

---

## Representation

- **City:** an integer index `0 .. num_cities-1`
- **Route:** a list of cities, e.g. `[2, 1, 3, 0]`
- **Pheromone matrix:** `pheromone[i][j]` stores trail strength from city *i* to city *j*

---

## Route length (fitness)

`route_length(route)` sums distances along consecutive edges:

- `sum(distances[route[i]][route[i+1]])` for `i = 0..n-2`

Shorter routes are better.

---

## How the next city is chosen

From a `current_city`, an ant chooses among *unvisited* cities using a probability proportional to:

- **pheromone influence**: `tau = pheromone[current_city][city] ** alpha`
- **heuristic influence (distance)**: `eta = (1 / distances[current_city][city]) ** beta`

Combined desirability:

- `value = tau * eta`

Then a roulette-wheel style sampling selects the next city.

---

## Pheromone update

After all ants build routes in an iteration:

### Evaporation
All pheromones are reduced:

- `pheromone[i][j] *= (1 - evaporation)`

### Deposit
Each ant deposits pheromone on the edges it used:

- `pheromone[a][b] += pheromone_deposit / length`

So **shorter routes deposit more pheromone**.

---

## Parameters (from `ant_colony_optimization.py`)

| Parameter | Value | Meaning |
|----------|-------|---------|
| `num_ants` | `10` | Ants per iteration |
| `num_iterations` | `50` | Number of ACO iterations |
| `alpha` | `1` | Pheromone importance |
| `beta` | `2` | Distance importance |
| `evaporation` | `0.5` | Evaporation rate |
| `pheromone_deposit` | `1` | Deposit factor (used as `1 / length`) |

---

## How to run

From the repository root:

```bash
python ant_colony_optimization/ant_colony_optimization.py
```

---

## Output

Each iteration prints the best route length found so far:

```
Iteration 1: Best length = ...
Iteration 2: Best length = ...
...
Iteration 50: Best length = ...

Best route found: [..]
Route length: ..
```

*(Exact results vary because the algorithm is stochastic.)*
