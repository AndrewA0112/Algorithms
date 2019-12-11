#!/usr/bin/python

import argparse

def find_max_profit(prices):
  profit = prices[1] - prices[0] # Sets PROFIT to second index - first index
  for index, p in enumerate(prices): # Loops through prices that also has indexes
    for pr in prices[:index]: # Loops through all prices before the current index and checks each one
      if p - pr > profit:
        profit = p - pr
  
  return profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))