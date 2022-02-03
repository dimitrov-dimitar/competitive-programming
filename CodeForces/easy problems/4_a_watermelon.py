# https://codeforces.com/problemset/problem/4/A

weight = int(input())

if weight == 2:
    print("NO")
elif weight == 4:
    print("YES")
elif weight % 2 == 0:
    print("YES")
else:
    print("NO")
