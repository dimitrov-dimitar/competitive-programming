# https://codeforces.com/problemset/problem/492/B

n, l = [int(x) for x in input().split()]
lanterns_coord = set([int(x) for x in input().split()])

lanterns_coord = sorted(lanterns_coord)
difference_number = []


for num in range(len(lanterns_coord) - 1):
    current_num = lanterns_coord[num]
    next_num = lanterns_coord[num + 1]
    difference_number.append((next_num - current_num) / 2)

difference_number = sorted(difference_number)

if 0 not in lanterns_coord:
    difference_number.append(lanterns_coord[0])
if lanterns_coord[-1] != l:
    difference_number.append(l - lanterns_coord[-1])

print(max(difference_number))
