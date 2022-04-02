# https://codeforces.com/problemset/problem/1283/A

t = int(input())

new_year_in_min = 1440

for _ in range(t):
    h, m = [int(x) for x in input().split()]
    current_min = h * 60 + m
    result = new_year_in_min - current_min
    print(result)
