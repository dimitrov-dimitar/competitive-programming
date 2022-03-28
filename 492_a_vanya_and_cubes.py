# https://codeforces.com/problemset/problem/492/A

n = int(input())

level = 0
bricks = 1
counter = 1

while n > 0:

    n -= bricks
    if n < 0:
        break
    level += 1
    counter += 1
    bricks += counter

print(level)
