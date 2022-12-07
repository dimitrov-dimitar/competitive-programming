import string

# Part One

matrix = []
counter = 0

with open("input") as f:
    for row in f:
        matrix.append(row.strip())


# vJrwpWtwJgWrhcsFMMfFFhFp
# vJrwpWtwJgWr
# hcsFMMfFFhFp

alphabet = list(string.ascii_lowercase + string.ascii_uppercase)
# print(alphabet)


for row in matrix:
    left, right = row[: len(row) // 2], row[len(row) // 2 :]
    for i in range(len(row) // 2):
        if left[i] in left and left[i] in right:
            counter += alphabet.index(left[i]) + 1
            break

print(counter)
