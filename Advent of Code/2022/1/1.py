# Part One

matrix = []

with open("input") as f:
    for row in f:
        if row == "\n":
            matrix.append("\n")
        else:
            matrix.append(int(row))

matrix.append("\n")
# print(matrix)

counter = 0
calories = 0
elves = {}

for row in matrix:
    if row != "\n":
        calories += row
    else:
        counter += 1
        elves[counter] = calories
        calories = 0

# print(elves)
max_num = max(elves, key=elves.get)
print(max_num)
print(elves[max_num])
