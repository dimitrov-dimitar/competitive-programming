# https://codeforces.com/problemset/problem/466/A

import math
n, m, a, b = [int(x) for x in input().split()]


prices_arr = []

prices_arr.append(n * a)

if n % m == 0:
    prices_arr.append(n // m * b)
else:
    reminder = n % m
    prices_arr.append((n // m * b) + (reminder * a))
    prices_arr.append(math.ceil(n / m) * b)

# print(prices_arr)
print(min(prices_arr))
