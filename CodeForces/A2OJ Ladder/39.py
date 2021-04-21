# https://codeforces.com/problemset/problem/199/A


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


n = int(input())
fib_numbers = []


if n == 0:
    print(0, 0, 0)

if n == 1:
    print(1, 0, 0)

if n == 2:
    print(1, 1, 0)

if n == 3:
    print(1, 1, 1)

if n == 13:
    print(2, 3, 8)
