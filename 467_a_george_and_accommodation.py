# https://codeforces.com/problemset/problem/467/A

n = int(input())

matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

counter = 0

for row in range(n):
    p = matrix[row][0]
    q = matrix[row][1]
    if q - p >= 2:
        counter += 1

print(counter)
