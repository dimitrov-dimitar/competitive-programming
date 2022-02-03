# https://codeforces.com/problemset/problem/1560/A

t = int(input())

num_arr = []
for x in range(1, 10000):
    if x % 3 != 0 and x % 10 != 3:
        num_arr.append(x)

for _ in range(t):
    k = int(input())
    print(num_arr[k - 1])
