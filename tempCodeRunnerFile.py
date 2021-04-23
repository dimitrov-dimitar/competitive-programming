# https://codeforces.com/problemset/problem/158/B

n = int(input())
s = [int(x) for x in input().split()]

print((sum(s) // 4) + 1)
