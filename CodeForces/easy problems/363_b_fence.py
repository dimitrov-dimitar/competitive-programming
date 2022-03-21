# https://codeforces.com/problemset/problem/363/B

n, k = [int(x) for x in input().split()]
h_arr = [int(x) for x in input().split()]

min_index = 0
first_arr = h_arr[:k]
first_sum = sum(first_arr)
min_sum = first_sum

if k == 1:
    print(h_arr.index(min(h_arr)) + 1)
else:
    for i in range(1, len(h_arr) - k + 1):
        current_sum = first_sum - h_arr[i - 1] + h_arr[i + k - 1]
        if current_sum < min_sum:
            min_sum = current_sum
            min_index = i
        first_sum = current_sum

    print(min_index + 1)
