# http://codeforces.com/problemset/problem/263/A
matrix = [list(map(int, input().split())) for i in range(5)]

# x = [x for x in matrix if 1 in x][0]
# print(x.index(1))

row_counter = 0

for i in range(5):
    if sum(matrix[i]) > 0:
        break
    row_counter += 1

col_counter = 0
for i in range(5):
    if matrix[row_counter][i] == 1:
        break
    col_counter += 1

row = abs(row_counter - 2)
col = abs(col_counter - 2)
print(row + col)
