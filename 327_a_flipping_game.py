# https://codeforces.com/problemset/problem/327/A

n = int(input())
n_arr = [int(x) for x in input().split()]

max_sum = -1
result = 0

if n == sum(n_arr):
    print(n - 1)
else:
    for i in range(n):
        for j in range(n):
            left_arr = n_arr[: i]
            mid_arr = n_arr[i : j + 1]
            right_arr = n_arr[j + 1 :]

            result = sum(left_arr) + sum(right_arr) + (len(mid_arr) - sum(mid_arr))
            if result > max_sum:
                max_sum = result
    print(max_sum)
