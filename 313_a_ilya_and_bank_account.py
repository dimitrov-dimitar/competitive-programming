# https://codeforces.com/problemset/problem/313/A

n = int(input())

if n >= 0:
    print(n)
elif n > -12:
    print(0)
else:
    last = abs(n) % 10
    print(last)
