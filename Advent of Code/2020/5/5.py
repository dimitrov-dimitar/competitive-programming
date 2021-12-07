matrix = []
row_matrix = [x for x in range(128)]
col_matrix = [x for x in range(8)]
board_pas = {}


with open('input') as f:
    for row in f:
        matrix.append(row)


for row in matrix:
    r = row_matrix
    c = col_matrix

    row_number = row[0:7]
    column_number = row[7:]
    for i in row_number:
        if i == "F":
            r = r[: len(r) // 2]
        else:
            r = r[len(r) // 2:]
    # print(r[0])

    for i in column_number:
        if i == "L":
            c = c[: len(c) // 2]
        else:
            c = c[len(c) // 2:]
    # print(c[0])

    board_pas[row] = r[0] * 8 + c[0]

# print(sorted(board_pas.values()))

sorted_board_pas = sorted(board_pas.values())
print(sorted_board_pas)


for number in sorted_board_pas:
    number += 1
    if number in sorted_board_pas:
        continue
    else:
        print(f'{number}')
        break
