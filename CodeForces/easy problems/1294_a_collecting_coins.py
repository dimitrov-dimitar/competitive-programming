# https://codeforces.com/problemset/problem/1294/A

t = int(input())

for _ in range(t):
    a, b, c, n = [int(x) for x in input().split()]
    result = (a + b + c + n) / 3
    if (a + b + c + n) % 3 == 0:
        if a > result or b > result or c > result:
            print("NO")
            continue
        print('YES')
    else:
        print("NO")
