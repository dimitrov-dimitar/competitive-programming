# https://codeforces.com/problemset/problem/791/A

limak_weight, bob_weight = [int(x) for x in input().split()]

years = 0

while limak_weight <= bob_weight:
    years += 1
    limak_weight *= 3
    bob_weight *= 2

print(years)
