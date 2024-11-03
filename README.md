# 5 Antenna Problem Solver using Genetic Algorithm

**Problem Statement**

The goal is to optimize the placement of 5 antennas on a 6x6 grid to maximize coverage. 

**Solution Approach**

A Genetic Algorithm is employed to solve this problem. The algorithm involves the following steps:

1. **Initialization:** A population of random antenna placements is generated.
2. **Fitness Evaluation:** Each individual's fitness is calculated based on the number of grid cells covered by the antennas.
3. **Selection:** The fittest individuals are selected for reproduction.
4. **Crossover:** Selected individuals are combined to create new offspring.
5. **Mutation:** Random changes are introduced to the offspring to maintain genetic diversity.
6. **Replacement:** The new generation replaces the old one.

**Implementation**

The Python code for this implementation includes the following functions:

* **`generate_population`:** Generates an initial population of random antenna placements.
* **`fitness_function`:** Calculates the fitness of an individual.
* **`selection`:** Selects the fittest individuals for reproduction.
* **`crossover`:** Combines two parent individuals to create offspring.
* **`mutation`:** Introduces random changes to an individual.
* **`main`:** The main function that controls the genetic algorithm's execution.

**Example Code**

```python
import random
import numpy as np

def generate_population(population_size):
    # ... implementation ...

def fitness_function(individual):
    # ... implementation ...

def selection(population, num_parents):
    # ... implementation ...

def crossover(parent1, parent2):
    # ... implementation ...

def mutation(individual, mutation_rate):
    # ... implementation ...

def main():
    # ... implementation ...

if __name__ == "__main__":
    main()
