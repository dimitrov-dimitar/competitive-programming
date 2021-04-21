matrix = []

with open('input') as f:
    for row in f:
        row_matrix = [x for x in row.split()]
        matrix.append(row_matrix)

# print(matrix)
counter = 0
abc_list = []
total = []

for row in matrix:
    # Empty line
    if not row:
        total.append(len(abc_list))
        # print(len(abc_list))
        abc_list = []
        continue

    for i in row:
        for ch in i:
            if ch not in abc_list:
                abc_list.append(ch)

print(sum(total))
