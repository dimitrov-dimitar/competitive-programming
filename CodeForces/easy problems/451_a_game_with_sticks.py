# https://codeforces.com/problemset/problem/451/A

n, m = [int(x) for x in input().split()]


min_num = min(n, m)
if min_num % 2 == 0:
    print('Malvika')
else:
    print('Akshat')
