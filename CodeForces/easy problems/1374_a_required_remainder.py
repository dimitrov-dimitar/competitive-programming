# https://codeforces.com/problemset/problem/1374/A

t = int(input())

for _ in range(t):
    x, y, n = [int(x) for x in input().split()]

    if n - n % x + y <= n:
        print(n - n % x + y)
    else:
        print(n - n % x - (x - y))
