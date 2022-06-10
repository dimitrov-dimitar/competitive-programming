# https://codeforces.com/problemset/problem/1358/A

t = int(input())

for _ in range(t):
    n, m = [int(x) for x in input().split()]

    production = n * m

    if production % 2 == 0:
        print(int(production / 2))
    else:
        print(int((production // 2)) + 1)
