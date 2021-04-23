# https://codeforces.com/problemset/problem/677/A

n, h = [int(x) for x in input().split()]
heights = list(map(int, input().split()))

total = 0

for height in heights:
    if height > h:
        total += 2
    else:
        total += 1

print(total)
