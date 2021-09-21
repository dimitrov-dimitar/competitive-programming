# https://codeforces.com/problemset/problem/758/A

n = int(input())
citizens = [int(x) for x in input().split()]
counter = 0

if n == 1:
    print(0)
else:
    max_citizens = max(citizens)

    for citizen in citizens:
        if citizen != max_citizens:
            counter += max_citizens - citizen
    print(counter)
