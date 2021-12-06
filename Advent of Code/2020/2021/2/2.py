# Part One
matrix = []

with open("input") as f:
    for row in f:
        matrix.append(row)

position_x = 0
position_y = 0

for row in matrix:
    position = row.split()[0]
    value = int(row.split()[1])
    if position == "forward":
        position_x += value
    elif position == "up":
        position_y += value
    else:
        position_y -= value

print(abs(position_x * position_y))

# Part Two

aim = 0
position_x = 0
position_y = 0

for row in matrix:
    position = row.split()[0]
    value = int(row.split()[1])
    if position == "down":
        aim += value
    elif position == "up":
        aim -= value
    else:
        position_x += value
        position_y += aim * value

print(abs(position_x * position_y))
