# https://codeforces.com/problemset/problem/1154/A

x_1, x_2, x_3, x_4 = [int(x) for x in input().split()]

list_num = [x_1, x_2, x_3, x_4]
list_num.sort()

max_num = list_num[-1]

for num in range(3):
    print(max_num - list_num[num], end=' ')
