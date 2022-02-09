# https://codeforces.com/problemset/problem/1475/A

t = int(input())

for _ in range(t):
    n = int(input())

    # Check n to be power of 2
    if n & (n - 1) == 0:
        print("NO")
    else:
        print("YES")
