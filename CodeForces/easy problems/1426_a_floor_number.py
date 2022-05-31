# https://codeforces.com/problemset/problem/1426/A

t = int(input())

for _ in range(t):
    n, x = [int(x) for x in input().split()]
    floor = 0
    apartment = 2

    while True:
        floor += 1
        if apartment >= n:
            print(floor)
            break
        apartment += x
