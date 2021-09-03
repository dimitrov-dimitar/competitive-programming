# https://codeforces.com/problemset/problem/189/A

n, a, b, c = [int(x) for x in input().split()]

pieces = sorted([a, b, c])
counter = 0
list_p = []


while n != 0:
    result = n // a
    list_p.append(result)
    n -= result
