# Part One

matrix = []

with open("input") as f:
    for row in f:
        matrix.append(row.strip())

# print(matrix)
points = 0

for row in matrix:
    opponent, me = row.split()
    # print(opponent, me)
    if me == "X":
        points += 1
    elif me == "Y":
        points += 2
    else:
        points += 3

    if opponent == "A" and me == "X":
        points += 3
    elif opponent == "A" and me == "Y":
        points += 6
    elif opponent == "B" and me == "Y":
        points += 3
    elif opponent == "B" and me == "Z":
        points += 6
    elif opponent == "C" and me == "Z":
        points += 3
    elif opponent == "C" and me == "X":
        points += 6

print(points)

# Part Two
points = 0

for row in matrix:
    opponent, me = row.split()

    # lose
    if me == "X":
        if opponent == "A":
            points += 3
        elif opponent == "B":
            points += 1
        elif opponent == "C":
            points += 2
    # draw
    elif me == "Y":
        if opponent == "A":
            points += 1
            points += 3
        elif opponent == "B":
            points += 2
            points += 3
        elif opponent == "C":
            points += 3
            points += 3
    # win
    elif me == "Z":
        if opponent == "A":
            points += 2
            points += 6
        elif opponent == "B":
            points += 3
            points += 6
        elif opponent == "C":
            points += 1
            points += 6

print(points)
