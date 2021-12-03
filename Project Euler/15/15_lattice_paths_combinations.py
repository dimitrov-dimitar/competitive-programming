# mathematical approuch (combinations)

from math import factorial

grid = 20
n = 2 * grid
k = grid
combinations = factorial(n) / (factorial(k) * factorial(n - k))

print(combinations)
