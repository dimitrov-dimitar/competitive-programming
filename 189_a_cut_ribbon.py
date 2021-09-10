# https://codeforces.com/problemset/problem/189/A

n, a, b, c = [int(x) for x in input().split()]

pieces = sorted([a, b, c], reverse=True)
counter = 0
list_p = []


