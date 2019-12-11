#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = None
  for r in recipe:
    if r not in ingredients: # Checks if the recipe ingredient is apart of the ingredients dict
      return 0
    if recipe[r] > ingredients[r]: # Checks if current ingredient has more than the current recipe
      return 0
    if batches is None: # For first case of batches
      batches = ingredients[r] // recipe[r]
    elif ingredients[r] // recipe[r] < batches: # Checks if the current recipe/ingredient is smaller than current batches count
      batches = ingredients[r] // recipe[r]
  return batches

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 232, 'butter': 100, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))