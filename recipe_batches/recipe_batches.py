#!/usr/bin/python

import math

# find items in recipe dictionary => 10 units of milk
# find items in ingredients dictionary => 20 units of milk
# divide ingredients by recipe (20/10 = 2)

def recipe_batches(recipe, ingredients):
  counter = math.inf

  for key in recipe:
    if ingredients.get(key) and ingredients[key] / recipe[key] >= 1:
      counter = min(counter, ingredients[key] // recipe[key])
    else:
      return 0

  return counter


# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))