# https://codeforces.com/problemset/problem/1328/A

import math

t = int(input())

# counter = 0

for _ in range(t):
    a, b = [int(x) for x in input().split()]
    # while a % b != 0:
    #     a += 1
    #     counter += 1
    # print(counter)
    # counter = 0

    if a % b == 0:
        print(0)
    else:
        result = math.ceil(a / b)
        result *= b
        print(result - a)
