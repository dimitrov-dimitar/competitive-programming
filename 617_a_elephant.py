# https://codeforces.com/problemset/problem/617/A

x = int(input())

counter = 0
steps = 0

if x <= 5:
    steps = 1
elif x % 5 == 0:
    steps = x / 5
else:
    steps = (x // 5) + 1

print(int(steps))
