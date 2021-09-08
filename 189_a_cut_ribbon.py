# https://codeforces.com/problemset/problem/189/A

n, a, b, c = [int(x) for x in input().split()]

pieces = sorted([a, b, c], reverse=True)
counter = 0
list_p = []


for p in pieces:
    result = n // p
    for _ in range(result):
        list_p.append(p)


print(list_p)
