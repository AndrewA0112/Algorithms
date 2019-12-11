#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

def eating_cookies(n, cache=None):
  cache = cache or [0 for i in range(n+1)]
  if n > 0:
    cache[0], cache[1] = 1, 1
  else:
    cache[0] = 1

  if cache[n] == 0:
    for i in range(1, min(n+1,4)):
      cache[n] += eating_cookies(n - i, cache)

  return cache[n]

# def eating_cookies(n, cache=None):
#   if n < 0: return 0
#   if n == 1 or n == 0: return 1
#   ways = 0
#   for i in range(1, min(n+1,4)):
#     # print(ways)
#     ways += eating_cookies(n - i)
#   return ways

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')