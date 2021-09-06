# https://codeforces.com/problemset/problem/472/A

from math import sqrt

n = int(input())


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True


x = 1
y = n - x

while True:
    x += 1
    y -= 1

    if not is_prime(x) and not is_prime(y):
        print(x, y, end=' ')
        break
