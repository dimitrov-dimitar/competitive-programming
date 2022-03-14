# https://codeforces.com/problemset/problem/1551/A

t = int(input())

for _ in range(t):
    n = int(input())
    c_1 = n // 3
    c_2 = n // 3

    if n == 1:
        print(1, 0)
        continue

    if c_1 + 2 * c_2 == n:
        print(c_1, c_2)
    else:
        c_2 += 1
        if c_1 + 2 * c_2 == n:
            print(c_1, c_2)
        elif c_2 + 2 * c_1 == n:
            print(c_2, c_1)
