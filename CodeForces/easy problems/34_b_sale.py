# https://codeforces.com/problemset/problem/34/B

n, m = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]

arr.sort()
result = 0
# print(abs(sum(arr[:m])))

for i in range(m):
    if arr[i] > 0:
        pass
    else:
        result += arr[i]

print(abs(result))
