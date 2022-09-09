# https://codeforces.com/problemset/problem/1/B

import string
from collections import deque

alphabet = list(string.ascii_uppercase)

# 2
# R23C55
# BC23


# R23C55 -> BC23
def from_r_c_to_letter(coordinates):
    result_arr = deque()
    result = ""
    left, right = coordinates.split("C")
    right = int(right)
    whole_num = right // 26
    reminder = right % 26
    if reminder == 0:
        whole_num -= 1
        reminder = 26
    result_arr.append(reminder)
    if whole_num > 26:
        while whole_num > 26:
            int_num = whole_num // 26
            reminder = whole_num % 26
            if reminder == 0:
                int_num -= 1
                reminder = 26
            result_arr.appendleft(reminder)
            if int_num < 27:
                result_arr.appendleft(int_num)
            whole_num = int_num
    else:
        if whole_num == 0:
            pass
        else:
            result_arr.appendleft(whole_num)
    for num in result_arr:
        result += alphabet[num - 1]
    result += left[1:]
    return result


# BC23 -> R23C55
def from_letter_to_r_c(coordinates):
    left = coordinates.rstrip("0123456789")
    right = coordinates[len(left) :]
    result = "R" + right + "C"
    result_arr = []
    for ch in left:
        idx = alphabet.index(ch) + 1
        result_arr.append(idx)
    left_result = 0
    while True:
        if len(result_arr) == 1:
            left_result = result_arr[0]
            break
        left_result = result_arr[0] * 26 + result_arr[1]
        result_arr.pop(0)
        result_arr[0] = left_result
    result += str(left_result)
    return result


n = int(input())

for _ in range(n):
    coordinates = input()
    check = "".join([i for i in coordinates if not i.isdigit()])
    if check == "RC" and coordinates[1].isdigit():
        print(from_r_c_to_letter(coordinates))
    else:
        print(from_letter_to_r_c(coordinates))
