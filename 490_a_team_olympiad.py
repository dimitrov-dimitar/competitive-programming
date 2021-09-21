# https://codeforces.com/problemset/problem/490/A

n = int(input())
childrens = [int(x) for x in input().split()]


if all(list(range(1, 4))) in childrens:
    print(1)
else:
    print(0)

