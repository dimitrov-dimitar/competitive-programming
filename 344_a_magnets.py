# https://codeforces.com/problemset/problem/344/A

n = int(input())

group = 1
matrix = []

for _ in range(n):
    magnet = input()
    matrix.append(magnet)

for element in range(n - 1):
    current_el = matrix[element][0]
    next_el = matrix[element + 1][0]
    if current_el != next_el:
        group += 1

print(group)
