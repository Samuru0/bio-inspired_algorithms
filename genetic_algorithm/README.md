# Genetic Algorithm (GA)

A bio-inspired search heuristic that mimics the process of **natural selection**. Candidate solutions (individuals) evolve over successive generations through selection, crossover, and mutation until an optimal (or near-optimal) solution emerges.

## Problem

Maximize **f(x) = x²**, where *x* is a non-negative integer encoded as a binary chromosome of `NUM_BITS` bits.

## How it works

| Step | Description |
|------|-------------|
| **Initialisation** | A random population of binary chromosomes is created. |
| **Fitness evaluation** | Each chromosome is decoded to an integer *x* and its fitness f(x) = x² is computed. |
| **Selection** | Parents are chosen via roulette-wheel (fitness-proportionate) selection. |
| **Crossover** | Two parents exchange genetic material at a random cut point to produce two offspring. |
| **Mutation** | Each gene is flipped with a small probability `MUTATION_RATE`. |
| **Replacement** | The offspring form the next generation and the cycle repeats. |

## Key Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `POPULATION_SIZE` | 10 | Number of individuals per generation |
| `NUM_BITS` | 5 | Chromosome length (x ∈ [0, 31]) |
| `NUM_GENERATIONS` | 20 | Number of evolutionary cycles |
| `CROSSOVER_RATE` | 0.8 | Probability that crossover occurs |
| `MUTATION_RATE` | 0.01 | Per-gene mutation probability |

## How to run

```bash
python genetic_algorithm.py
```

## Example output

```
=============================================
       Genetic Algorithm — f(x) = x²
=============================================
Generation  1 | Best x = 28 | f(x) =  784 | Chromosome: 11100
Generation  2 | Best x = 30 | f(x) =  900 | Chromosome: 11110
...
Generation 20 | Best x = 31 | f(x) =  961 | Chromosome: 11111
=============================================
Best solution found: x = 31, f(x) = 961
=============================================
```
