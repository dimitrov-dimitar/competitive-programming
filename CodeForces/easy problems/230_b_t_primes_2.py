# https://codeforces.com/problemset/problem/230/B

from math import sqrt

n = int(input())
numbers = [int(x) for x in input().split()]


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


def solve(n):
    sq = int(sqrt(n))
    if sq ** 2 != n:
        return False

    if is_prime(sq):
        return True
    else:
        return False


for number in numbers:
    if solve(number):
        print("YES")
    else:
        print("NO")
