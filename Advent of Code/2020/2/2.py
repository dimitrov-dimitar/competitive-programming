with open('input') as f:
    data = f.readlines()

# Example - 7-11 g: xzgnggggrggrg
# Part One

number_part = [i.split(' ')[0] for i in data]

min_num = [i.split('-')[0] for i in number_part]
max_num = [i.split('-')[1] for i in number_part]

key = [i.split(':')[0][-1] for i in data]
value = [i.split(':')[1] for i in data]

counter_1 = 0

for i in range(len(value)):
    substring_in_string = value[i].count(f'{key[i]}')
    if int(min_num[i]) <= substring_in_string <= int(max_num[i]):
        counter_1 += 1

print(counter_1)

# Part Two
counter_2 = 0

for i in range(len(value)):
    a = key[i]
    b = value[i][int(min_num[i])]
    c = value[i][int(max_num[i])]

    # if a == b ^ a == c:
    if (a == b and a != c) or (a != b and a == c):
        counter_2 += 1

print(counter_2)
