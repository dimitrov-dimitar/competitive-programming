# https://codeforces.com/problemset/problem/581/A

a, b = [int(x) for x in input().split()]

min_num = min(a, b)
max_num = max(a, b)

result = max_num - min_num

if result < 2:
    result = 0
else:
    result /= 2

print(min_num, int(result), end=" ")
