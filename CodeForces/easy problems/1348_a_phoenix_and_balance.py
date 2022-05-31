# https://codeforces.com/problemset/problem/1348/A

t = int(input())

for _ in range(t):
    n = int(input())
    A = 0
    B = 0

    for i in range(1, n // 2):
        A += 2**i

    for i in range(n // 2, n):
        B += 2**i

    result = (2**n + A) - B
    print(result)
