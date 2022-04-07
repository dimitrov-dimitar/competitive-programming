# https://codeforces.com/problemset/problem/1311/A

t = int(input())

for _ in range(t):
    a, b = [int(x) for x in input().split()]

    if a == b:
        print(0)
    elif a > b:
        result = a - b
        if result % 2 == 0:
            print(1)
        else:
            print(2)
    else:
        result = b - a
        if result % 2 == 1:
            print(1)
        else:
            print(2)
