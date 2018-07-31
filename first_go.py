
import random

population = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
target = 'guess me'

def generate_random_word(target_length):
  
  guess = []
   while len(guess) < target_length:  # using while loop in case the target word is longer than the population.
      size_of_guess = min(target_length - len(guess), len(population)) # this would help keeping the guessed word size within the size of population.
      guess.extend(random.sample(population,size_of_guess))
   return "".join(guess)

