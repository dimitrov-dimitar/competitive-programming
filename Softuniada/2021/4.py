r, c = [int(x) for x in input().split()]

matrix = []

for row in range(r):
    row_input = [x for x in input().split()]
    matrix.append(row_input)

# print(matrix)

symbol_found = input()
initial_r, initial_c = [int(x) for x in input().split()]
initial_symbol = matrix[initial_r][initial_c]
new_initial = initial_symbol
original_r = initial_r
original_c = initial_c
# print(initial_symbol)


def up_move(initial_r, initial_c):
    # up
    while True:
        initial_r -= 1
        if initial_r > r - 1 or initial_r < 0:
            break
        current_pos = matrix[initial_r][initial_c]
        if current_pos == new_initial:
            matrix[initial_r][initial_c] = symbol_found
        if current_pos == symbol_found:
            solve(initial_r, initial_c)
        else:
            break


def down_move(initial_r, initial_c):
    # down
    while True:
        initial_r += 1
        if initial_r > r - 1 or initial_r < 0:
            break
        current_pos = matrix[initial_r][initial_c]
        if current_pos == new_initial:
            matrix[initial_r][initial_c] = symbol_found
        if current_pos == symbol_found:
            solve(initial_r, initial_c)
        else:
            break


def left_move(initial_r, initial_c):
    # left
    while True:
        initial_c -= 1
        if initial_c > c - 1 or initial_c < 0:
            break
        current_pos = matrix[initial_r][initial_c]
        if current_pos == new_initial:
            matrix[initial_r][initial_c] = symbol_found
        if current_pos == symbol_found:
            solve(initial_r, initial_c)
        else:
            break


def right_move(initial_r, initial_c):
    # right
    while True:
        initial_c += 1
        if initial_c > c - 1 or initial_c < 0:
            break
        current_pos = matrix[initial_r][initial_c]
        if current_pos == new_initial:
            matrix[initial_r][initial_c] = symbol_found
        if current_pos == symbol_found:
            solve(initial_r, initial_c)
        else:
            break


def solve(initial_r, initial_c):
    while up_move(initial_r, initial_c) or down_move(initial_r, initial_c) or left_move(initial_r, initial_c) or right_move(initial_r, initial_c):
        up_move(initial_r, initial_c)
        down_move(initial_r, initial_c)
        left_move(initial_r, initial_c)
        right_move(initial_r, initial_c)


solve(initial_r, initial_c)

# while up_move(initial_r, initial_c) or down_move(initial_r, initial_c) or left_move(initial_r, initial_c) or right_move(initial_r, initial_c):
#     up_move(initial_r, initial_c)
#     down_move(initial_r, initial_c)
#     left_move(initial_r, initial_c)
#     right_move(initial_r, initial_c)

# while up_move(initial_r, initial_c) or down_move(initial_r, initial_c) or left_move(initial_r, initial_c) or right_move(initial_r, initial_c):
#     up_move(initial_r, initial_c)
#     down_move(initial_r, initial_c)
#     left_move(initial_r, initial_c)
#     right_move(initial_r, initial_c)

# while up_move(initial_r, initial_c) or down_move(initial_r, initial_c) or left_move(initial_r, initial_c) or right_move(initial_r, initial_c):
#     up_move(initial_r, initial_c)
#     down_move(initial_r, initial_c)
#     left_move(initial_r, initial_c)
#     right_move(initial_r, initial_c)

matrix[original_r][original_c] = symbol_found

# print(matrix)
for r in matrix:
    for c in r:
        print(c, end='')
    print()
# print('test')
