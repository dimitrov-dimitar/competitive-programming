# https://codeforces.com/problemset/problem/1335/A

t = int(input())

for _ in range(t):
    n = int(input())
    if n % 2 == 0:
        result = int(n / 2 - 1)
        print(result)
    else:
        result = int(n // 2)
        print(result)
