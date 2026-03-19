# Particle Swarm Optimization (PSO)

A computational method inspired by the **social behaviour of bird flocking and fish schooling**. A swarm of particles explores the search space; each particle is attracted toward its own best known position and toward the best position found by the entire swarm.

## Problem

Minimize the **Sphere function**: f(**x**) = Σ xᵢ², whose global minimum is **0** at the origin.

## How it works

| Step | Description |
|------|-------------|
| **Initialisation** | Particles are placed at random positions with random velocities within the search bounds. |
| **Velocity update** | Each particle's velocity is adjusted using an *inertia* term, a *cognitive* term (pull toward personal best), and a *social* term (pull toward global best). |
| **Position update** | Particles move according to their updated velocities; positions are clamped to the search bounds. |
| **Evaluation** | Fitness is computed; personal and global bests are updated if a better position is found. |
| **Iteration** | The process repeats until convergence or the iteration limit is reached. |

## Key Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `NUM_PARTICLES` | 20 | Swarm size |
| `NUM_DIMENSIONS` | 3 | Dimensionality of the search space |
| `NUM_ITERATIONS` | 50 | Number of PSO cycles |
| `BOUNDS` | (-5.12, 5.12) | Search space bounds per dimension |
| `W` | 0.5 | Inertia weight |
| `C1` | 1.5 | Cognitive (personal best) coefficient |
| `C2` | 1.5 | Social (global best) coefficient |

## How to run

```bash
python particle_swarm_optimization.py
```

## Example output

```
=======================================================
   Particle Swarm Optimization — Sphere Function
=======================================================
Iteration   1 | Best fitness: 0.523419 | Position: [0.1234, -0.4567, 0.5678]
Iteration   2 | Best fitness: 0.312104 | Position: [0.0891, -0.2134, 0.4901]
...
Iteration  50 | Best fitness: 0.000012 | Position: [0.001234, -0.000567, 0.002789]
=======================================================
Best solution found:
  Position: [0.001234, -0.000567, 0.002789]
  f(x)    : 0.000012
=======================================================
```
