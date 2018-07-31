
import random

population = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
target = 'guess me'

def generate_random_word(target_length):
  
  guess = []
   while len(guess) < target_length:  # using while loop in case the target word is longer than the population.
      size_of_guess = min(target_length - len(guess), len(population)) # this would help keeping the guessed word size within the size of population.
      guess.extend(random.sample(population,size_of_guess))
   return "".join(guess)

def fitness_value(guess):
  return sum(1 for expected, actual in zip(target,guess) if expected == actual)

def mutation(parent):
    index = random.randrange(0,len(parent))
    childGenes = list(parent)
    newGene, alternate = random.sample(geneSet,2)
    childGenes[index] = alternate if newGene == childGenes[index] else newGene # to ensure new gene is introduced.
    return "".join(childGenes) 
  
  


