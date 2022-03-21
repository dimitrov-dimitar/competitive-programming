# https://codeforces.com/problemset/problem/935/A

n = int(input())

counter = 0

for i in range(1, n):
    remainder = n - i
    if remainder % i == 0:
        counter += 1

print(counter)
