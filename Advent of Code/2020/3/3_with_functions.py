matrix = []

with open('input') as f:
    for row in f:
        row_matrix = [x for x in row if x != '\n']
        row_matrix *= 1000
        matrix.append(row_matrix)

# print(matrix[0])

i, j = 0, 0
counter_1 = 0

# Part One

# 3, 1
while True:
    if i == len(matrix):
        break
    if matrix[i][j] == '#':
        counter_1 += 1
    i += 1
    j += 3

print(counter_1)


# Part Two

def boundary(i, j):
    if i >= len(matrix):
        return True


def solve(right, down, i=0, j=0, counter=0):
    while True:
        if boundary(i, j):
            break
        if matrix[i][j] == '#':
            counter += 1
        i += down
        j += right
    return counter


c_1 = solve(1, 1)
c_2 = solve(3, 1)
c_3 = solve(5, 1)
c_4 = solve(7, 1)
c_5 = solve(1, 2)


print(c_1 * c_2 * c_3 * c_4 * c_5)
