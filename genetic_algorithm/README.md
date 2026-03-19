# Simple Genetic Algorithm (SGA) — Evolving a Target String

This folder contains a **Simple Genetic Algorithm** implementation (`sga_es.py`) that evolves a population of strings until it matches a **target phrase**.

Unlike some classic GA examples (binary chromosomes + crossover), this version focuses on:
- **Fitness by character matching**
- **Elitism**
- **Mutation-only reproduction** (no crossover)

---

## Problem

Evolve a random string into the target:

- `TARGET = "HOLA MUNDO"`

Each individual is a string of the same length as `TARGET`, built from the gene set:

- `GENES = A–Z` plus space (`" "`)

---

## Representation

- **Individual (chromosome):** a string, e.g. `"HQZA MUNXO"`
- **Gene:** a single character (letter or space)
- **Population:** list of individuals (strings)

---

## Fitness function

The fitness is the **number of characters that match the target in the correct position**.

For an individual `s`:

- `fitness(s) = count of i where s[i] == TARGET[i]`

Maximum fitness is `len(TARGET)`.

---

## Genetic operators

### Selection (parent choice)
After sorting the population by fitness (descending), a parent is chosen randomly from the **top 50** individuals:

- `parent = random.choice(population[:50])`

### Mutation
Each character has a small probability of being replaced by a random gene:

- probability = `MUTATION_RATE`
- replacement comes from `GENES`

### Elitism
The best `ELITE_SIZE` individuals are copied directly into the next generation:

- `next_generation = population[:ELITE_SIZE]`

The rest of the next generation is filled with mutated children.

---

## Key parameters (from `sga_es.py`)

| Parameter | Value | Meaning |
|----------|-------|---------|
| `TARGET` | `"HOLA MUNDO"` | Target phrase to evolve |
| `POPULATION_SIZE` | `200` | Individuals per generation |
| `MUTATION_RATE` | `0.01` | Per-character mutation probability |
| `ELITE_SIZE` | `20` | Number of best individuals preserved |
| Parent pool | Top `50` | Parents sampled from best 50 individuals |
| `GENES` | `A-Z` + space | Allowed characters |

---

## Termination condition

The algorithm stops when the best individual reaches perfect fitness:

- `fitness(best) == len(TARGET)`

At that point, the best evolved string equals the target.

---

## How to run

From the repository root:

```bash
python genetic_algorithm/sga_es.py
```

---

## Example output (format)

Each generation prints the best current individual and its fitness:

```
Generation 1:  XQTA MUNDP | Fitness: 2
Generation 2:  HOTA MUNDP | Fitness: 8
...
Generation N:  HOLA MUNDO | Fitness: 9

Target string evolved successfully!
```

*(Your generations and intermediate strings will differ due to randomness.)*

---

## Notes / tips

- If you reduce `POPULATION_SIZE` too much, convergence may become very slow (or appear “stuck”) depending on randomness and parameter choices.
- This implementation is intentionally simple for learning: it demonstrates how **selection pressure + elitism + mutation** can drive improvement even without crossover.
