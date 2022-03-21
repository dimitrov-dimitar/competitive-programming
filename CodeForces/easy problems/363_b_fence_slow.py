# https://codeforces.com/problemset/problem/363/B

n, k = [int(x) for x in input().split()]
h_arr = [int(x) for x in input().split()]

min_sum = 99999999999
min_index = 0

for i in range(0, len(h_arr) - k + 1):
    current_sum = sum(h_arr[i : i + k])
    if current_sum < min_sum:
        min_sum = current_sum
        min_index = i

print(min_index + 1)
