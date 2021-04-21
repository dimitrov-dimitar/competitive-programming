# http://codeforces.com/problemset/problem/450/A

from collections import deque
from math import ceil
# n, m = [int(x) for x in input().split()]
n, m = map(int, input().split())
candies = [int(x) for x in input().split()]

# children = deque([int(x) for x in range(1, n + 1)])
# home = []

max_num = 0
counter = 0
candies_dict = {}

for k in candies:
    counter += 1
    candies_dict[counter] = k


for i in candies:
    result = ceil(i / m)
    if result >= max_num:
        max_num = result
        max_candies = i

# print(candies_dict)
# print(max_candies)

max_keys = []

for k, v in candies_dict.items():
    if v == max_candies:
        max_keys.append(k)

print(max_keys[-1])
