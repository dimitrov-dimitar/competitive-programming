matrix = []

with open("input") as f:
    for row in f:
        row_matrix = [x for x in row if x != "\n"]
        row_matrix *= 1000
        matrix.append(row_matrix)

# print(matrix[0])

i, j = 0, 0
counter_1 = counter_2 = counter_3 = counter_4 = counter_5 = 0

# Part One

# 3, 1
while True:
    if i >= len(matrix):
        break
    if matrix[i][j] == "#":
        counter_1 += 1
    i += 1
    j += 3

print(counter_1)


# Part Two

# 1, 1
i, j = 0, 0

while True:
    if i >= len(matrix):
        break
    if matrix[i][j] == "#":
        counter_2 += 1
    i += 1
    j += 1

print(counter_2)


# 5, 1
i, j = 0, 0

while True:
    if i >= len(matrix):
        break
    if matrix[i][j] == "#":
        counter_3 += 1
    i += 1
    j += 5

print(counter_3)

# 7, 1
i, j = 0, 0

while True:
    if i >= len(matrix):
        break
    if matrix[i][j] == "#":
        counter_4 += 1
    i += 1
    j += 7

print(counter_4)

# 1, 2
i, j = 0, 0

while True:
    if i >= len(matrix):
        break
    if matrix[i][j] == "#":
        counter_5 += 1
    i += 2
    j += 1

print(counter_5)


print(counter_1 * counter_2 * counter_3 * counter_4 * counter_5)
