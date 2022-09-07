# https://codeforces.com/problemset/problem/1560/B

t = int(input())

for _ in range(t):
    a, b, c = [int(x) for x in input().split()]
    total_num = 2 * (abs(a - b))
    if c > total_num or a > total_num or b > total_num or abs(a - b) == 1:
        print(-1)
    else:
        d = abs(a - b) + c
        if d > total_num:
            d = abs(abs(a - b) - c)
        print(d)
