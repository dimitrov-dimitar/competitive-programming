# https://codeforces.com/problemset/problem/731/A

import string

name = input()

eng_alphabet = list(string.ascii_lowercase)
current_position = 0
rotations = 0

for c in name:
    clock_rotation = 0
    clock_counter = 0

    c_position = eng_alphabet.index(c)

    # Clockwise
    min_pos = min(current_position, c_position)
    max_pos = max(current_position, c_position)

    for i in range(min_pos, max_pos):
        clock_rotation += 1

    # Counter clockwise
    clock_counter = 26 - clock_rotation

    rotations += min(clock_rotation, clock_counter)
    current_position = c_position

print(rotations)
