# https://codeforces.com/problemset/problem/158/A

n, k = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]

target = arr[k - 1]

result = list(filter(lambda x: x >= target and x != 0, arr))

print(len(result))
