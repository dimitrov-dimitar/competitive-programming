# https://codeforces.com/problemset/problem/456/A

n = int(input())

min_price = 0
state_var = False

for _ in range(n):
    a, b = [int(x) for x in input().split()]
    if a < b:
        state_var = True

if state_var:
    print("Happy Alex")
else:
    print("Poor Alex")
