# https://codeforces.com/problemset/problem/1537/A

t = int(input())

for _ in range(t):
    n = int(input())
    a_arr = [int(x) for x in input().split()]

    if sum(a_arr) / n == 1:
        print(0)
    else:
        x = (n + 1) - sum(a_arr)
        print(abs(x) + 1)
