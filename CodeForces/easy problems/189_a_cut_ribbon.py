# https://codeforces.com/problemset/problem/189/A

n, a, b, c = [int(x) for x in input().split()]

num_arr = [-1000000] * (n + 1)
num_arr[0] = 0

for i in range(a, n + 1):
    num_arr[i] = max(num_arr[i], num_arr[i - a] + 1)
for i in range(b, n + 1):
    num_arr[i] = max(num_arr[i], num_arr[i - b] + 1)
for i in range(c, n + 1):
    num_arr[i] = max(num_arr[i], num_arr[i - c] + 1)

print(num_arr[-1])
