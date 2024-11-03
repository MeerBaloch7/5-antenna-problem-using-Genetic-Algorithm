import random
import numpy as np
def generate_population(size):

    pop=[]
    for i in range(size):
      chromosome = [(random.randint(1, 6), random.randint(1, 6)) for _ in range(6)]
       
      pop.append(chromosome)
    return pop

def fitness(chromosome):
  grid = np.zeros((6, 6))
  for i in chromosome:
    x, y = i
    X,Y= x-1,y-1
    grid[X][Y] = 1
    if X>0:
        grid[X-1][Y] = 1
    if X<5:
        grid[X+1][Y] = 1
    if Y>0:
        grid[X][Y-1] = 1
    if Y<5:
        grid[X][Y+1] = 1

  return int(np.sum(grid))
  

def selection(population):
  population.sort(key=lambda x: fitness(x), reverse=True)
  return population[:10]
     

def crossover(chromosome1, chromosome2):
  crossover_point = 3
  child1 = chromosome1[:crossover_point] + chromosome2[crossover_point:]
  child2 = chromosome2[:crossover_point] + chromosome1[crossover_point:]
  return child1, child2

def mutation(chromosome):
  mutated_chromosome = []
  for x, y in chromosome:
    if y == 1:
      y = 6
    else:
      y -= 1
    mutated_chromosome.append((x, y))
  return mutated_chromosome

def Genetic_algorithm(population):
  
    selected = selection(population)
    cross_overed = []

    for i in range(len(selected)):
        # Get the next index, wrapping around to the first chromosome
        next_index = (i + 1) % len(selected)
        cross_overed.extend(crossover(selected[i], selected[next_index]))

    mutated = [mutation(i) for i in cross_overed]
    new_generation = mutated

    return new_generation

# solution to display
def solution(individual):
  grid = np.zeros((6, 6))
  for i in individual:
    x, y = i
    X,Y= x-1,y-1
    grid[X][Y] = 1
    if X>0:
        grid[X-1][Y] = 1
    if X<5:
        grid[X+1][Y] = 1
    if Y>0:
        grid[X][Y-1] = 1
    if Y<5:
        grid[X][Y+1] = 1
  print(grid)
  return grid

def solution_display(population,to_print=True):
    for individual in population:
        score= fitness(individual)
        if to_print:
            print(f'{individual}, Score: {score}')
        if score==24:
            if to_print:
                print('Solution found')
                print(f'Score: {score}')
                solution(individual)
            return True
        
    if to_print:
        print('Solution not found')
    return False

def main():
    generation=0
    population = generate_population(20)
    while not solution_display(population):
       print(f'Generation: {generation}')
       solution_display(population)
       population = Genetic_algorithm(population)
       generation+=1

main()

   



      
    