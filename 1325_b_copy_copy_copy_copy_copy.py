# https://codeforces.com/problemset/problem/1325/B

t = int(input())

for _ in range(t):
    n = int(input())
    a_arr = [int(x) for x in input().split()]
    a_arr.sort()
    a_arr = list(set(a_arr))
    print(len(a_arr))
