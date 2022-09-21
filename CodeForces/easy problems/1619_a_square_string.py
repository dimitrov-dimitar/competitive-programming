# https://codeforces.com/problemset/problem/1619/A

t = int(input())

for _ in range(t):
    s = input()
    if len(s) % 2 == 0:
        mid = int(len(s) / 2)
        left = s[:mid]
        right = s[mid:]
        if left == right:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
