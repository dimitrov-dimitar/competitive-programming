# https://codeforces.com/problemset/problem/1/A

import math

n, m, a = map(int, input().split())
# n, m, a = [int(x) for x in input().split()]

w = math.ceil(n / a)
h = math.ceil(m / a)

print(w * h)
