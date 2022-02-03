# https://codeforces.com/problemset/problem/469/A

n = int(input())

little_x = [int(x) for x in input().split()]
little_y = [int(x) for x in input().split()]

concat_list = list(set(little_x[1:] + little_y[1:]))
input_list = list(range(1, n + 1))

if 0 in concat_list:
    concat_list.remove(0)

if concat_list == input_list:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
