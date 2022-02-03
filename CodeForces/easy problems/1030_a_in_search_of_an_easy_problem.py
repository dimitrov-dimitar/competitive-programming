# https://codeforces.com/problemset/problem/1030/A

n = int(input())
cordinators = [int(x) for x in input().split()]


if sum(cordinators) > 0:
    print("HARD")
else:
    print("EASY")
