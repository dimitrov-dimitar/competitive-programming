# https://codeforces.com/problemset/problem/500/A

n, t = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]

next = 0
exit_var = ""

i = 1

while True:
    if i > t or i > len(arr):
        exit_var = "NO"
        break

    next = i + arr[i - 1]

    if next == t:
        exit_var = "YES"
        break
    i = next


print(exit_var)
