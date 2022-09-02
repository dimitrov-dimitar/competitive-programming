# https://codeforces.com/problemset/problem/1/B

import string

alphabet = list(string.ascii_uppercase)

# 2
# R23C55
# BC23


def from_r_c_to_letter(coordinates):
    result = ""
    left, right = coordinates.split("C")
    right = int(right)
    letter_count = right // 26
    if letter_count == 0:
        letter_count = 1
    # return letter_count
    reminder = right % 26
    result += alphabet[letter_count - 1]
    result += alphabet[reminder - 1]
    result += left[1:]
    return result


def from_letter_to_r_c(coordinates):
    pass


n = int(input())


for _ in range(n):
    coordinates = input()
    if coordinates[0] == "R":
        print(from_r_c_to_letter(coordinates))
    else:
        print(from_letter_to_r_c(coordinates))
