# https://codeforces.com/problemset/problem/43/A

n = int(input())
arr = []

for _ in range(n):
    arr.append(input())

print(max(set(arr), key=arr.count))
