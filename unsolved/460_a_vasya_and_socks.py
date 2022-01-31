# https://codeforces.com/problemset/problem/460/A

n, m = [int(x) for x in input().split()]

days = n

while True:
    add_days = n // m
    if add_days == 0:
        break
    days += add_days
    n = add_days

while days % m == 0:
    days += 1

print(days)
