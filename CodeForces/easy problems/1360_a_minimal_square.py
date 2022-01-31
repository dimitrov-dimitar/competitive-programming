# https://codeforces.com/problemset/problem/1360/A

t = int(input())
for _ in range(t):
    a, b = [int(x) for x in input().split()]
    first_sqr = (2 * min(a, b)) ** 2
    second_sqr = max(a, b) ** 2
    print(max(first_sqr, second_sqr))
