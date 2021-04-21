# http://codeforces.com/problemset/problem/248/A

n = int(input())

left_side = []
right_side = []

for cupboard in range(n):
    l_r = input().split()
    left = int(l_r[0])
    right = int(l_r[1])
    left_side.append(left)
    right_side.append(right)


sum_l = sum(left_side)
sum_r = sum(right_side)

if sum_l <= len(left_side) / 2:
    left = sum_l
else:
    left = len(left_side) - sum_l

if sum_r <= len(right_side) / 2:
    right = sum_r
else:
    right = len(right_side) - sum_r

print(left + right)
