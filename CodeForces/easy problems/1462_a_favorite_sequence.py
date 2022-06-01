# https://codeforces.com/problemset/problem/1462/A

t = int(input())

for _ in range(t):
    len_arr = int(input())
    n = [int(x) for x in input().split()]

    result_arr = []

    for i in range(len_arr):
        if i % 2 == 0:
            result_arr.append(n.pop(0))
        else:
            result_arr.append(n.pop(-1))

    result_arr_str = map(str, result_arr)
    print(" ".join(result_arr_str))
