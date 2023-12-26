matrix = []

with open("input.txt", mode="r") as f:
    for row in f:
        matrix.append(row.strip())

# Part One
total_sum = 0
two_digit_num_arr = []
left_num = 0
right_num = 0

for row in matrix:
    # left num
    for ch in row:
        if ch.isdigit():
            left_num = ch
            break

    # right num
    for ch in row[::-1]:
        if ch.isdigit():
            right_num = ch
            break
    two_digit_num = int(left_num + right_num)
    two_digit_num_arr.append(two_digit_num)


print(sum(two_digit_num_arr))

# Part Two
two_digit_num_arr = []
row_arr = []
string_nums_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

for row in matrix:
    for num in string_nums_dict.keys():
        if num in row:
            while num in row:
                position = row.find(num)
                row_arr.append(str(num) + "-" + str(position))
                row = row.replace(num, "*" * len(num), 1)
            row = row.replace("*" * len(num), num)

    for count, ch in enumerate(row):
        if ch.isdigit():
            row_arr.append(str(ch) + "-" + str(count))
    sorted_row_arr = sorted(row_arr, key=lambda x: int(x.split("-")[1]))

    left_num = sorted_row_arr[0].split("-")[0]
    if left_num.isdigit():
        pass
    else:
        left_num = string_nums_dict[left_num]

    right_num = sorted_row_arr[-1].split("-")[0]
    if right_num.isdigit():
        pass
    else:
        right_num = string_nums_dict[right_num]

    two_digit_num = int(str(left_num) + str(right_num))
    two_digit_num_arr.append(two_digit_num)

    row_arr = []

print(sum(two_digit_num_arr))
