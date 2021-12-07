# Part One
matrix = []

with open("input") as f:
    for row in f:
        matrix.append(int(row))

counter = 0

for num in range(len(matrix) - 1):
    current = matrix[num]
    next_ = matrix[num + 1]
    if current < next_:
        counter += 1

print(counter)

# Part Two
counter_two = 0

for num in range(0, len(matrix) - 3):
    a = matrix[num]
    b = matrix[num + 1]
    c = matrix[num + 2]
    d = matrix[num + 3]

    current = a + b + c
    next_ = b + c + d
    if current < next_:
        counter_two += 1

print(counter_two)
