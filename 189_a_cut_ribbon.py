# https://codeforces.com/problemset/problem/189/A

n, a, b, c = [int(x) for x in input().split()]

pieces = sorted([a, b, c])
counter = 0

# a, a + b, a + c
# b, b + c
# c

