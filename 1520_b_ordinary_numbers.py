# https://codeforces.com/problemset/problem/1520/B

t = int(input())

for _ in range(t):
    n = input()
    k = len(n)
    n = int(n)
    p = int("1" * k)
    a = n // p + 9 * (k - 1)
    print(a)
