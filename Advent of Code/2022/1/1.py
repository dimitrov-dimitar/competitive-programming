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
print(max(elves.values()))

# Part Two

new_dict = dict(sorted(elves.items(), key=lambda item: item[1]))
# print(new_dict)

top_three_elves = (
    list(new_dict.values())[-1]
    + list(new_dict.values())[-2]
    + list(new_dict.values())[-3]
)

print(top_three_elves)
