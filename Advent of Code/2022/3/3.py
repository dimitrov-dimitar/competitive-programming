import string
from collections import Counter

# Part One

matrix = []
counter = 0

with open("input_test") as f:
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

# Part Two

counter = 0
counter_group = 0
first_group = ""
first_group_arr = []

for row in matrix:
    if counter_group == 3:
        x = Counter(first_group)
        print(Counter(first_group_arr[0]))
        print(Counter(first_group_arr[1]))
        print(Counter(first_group_arr[2]))
        # for i in Counter(first_group):
        #     print(i)
        first_group = ""
        first_group_arr = []
        counter_group = 0

    first_group += row
    first_group_arr.append(row)
    counter_group += 1
