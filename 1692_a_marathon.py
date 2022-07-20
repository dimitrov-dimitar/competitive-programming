# https://codeforces.com/problemset/problem/1692/A

t = int(input())

for _ in range(t):
    distances = [int(x) for x in input().split()]
    a, b, c, d = distances
    sort_distances = sorted(distances, reverse=True)
    print(sort_distances.index(a))
