# Particle Swarm Optimization (PSO)

Particle Swarm Optimization is inspired by **collective behavior** (e.g., bird flocks / fish schools). A group of particles explores the search space while sharing information about the best solutions found.

This implementation is a minimal, educational PSO in **one dimension (1D)**.

---

## Problem (in this code)

Minimize:

- `f(x) = x^2`

The global minimum is:

- `x = 0` with `f(0) = 0`

---

## Representation

Each particle has:
- **position**: a float `x`
- **velocity**: a float `v`
- **personal best**: `p_best[i]` (best position particle *i* has found)
- **global best**: `g_best` (best position found by any particle)

---

## Initialization

- positions sampled uniformly from `[-10, 10]`
- velocities sampled uniformly from `[-1, 1]`

Personal bests start at the initial positions, and the global best is the best among them.

---

## Core update equations

For each iteration and each particle:

### Velocity update
```
v = w*v + c1*r1*(p_best - x) + c2*r2*(g_best - x)
```

Where:
- `w` = inertia term
- `c1` = cognitive coefficient (pull toward personal best)
- `c2` = social coefficient (pull toward global best)
- `r1`, `r2` are random numbers in `[0, 1]`

### Position update
```
x = x + v
```

Then the objective function is evaluated, and `p_best` / `g_best` are updated if improvements are found.

> Note: this script does **not** clamp positions to a bound after updating them.

---

## Parameters (from `pso.py`)

| Parameter | Value | Meaning |
|----------|-------|---------|
| `num_particles` | `20` | Swarm size |
| `num_iterations` | `50` | Number of iterations |
| `w` | `0.5` | Inertia weight |
| `c1` | `1.5` | Cognitive coefficient |
| `c2` | `1.5` | Social coefficient |

---

## How to run

From the repository root:

```bash
python particle_swarm_optimization/pso.py
```

---

## Output

Each iteration prints the best position found so far:

```
Iteration 1: Best = -0.5321
Iteration 2: Best = 0.1044
...
Iteration 50: Best = 0.0000

Best solution found: 0.0000
```

*(Exact results vary due to randomness.)*
