# http://codeforces.com/problemset/problem/112/A

s_1 = input().lower()
s_2 = input().lower()

if s_1 < s_2:
    print("-1")
elif s_2 < s_1:
    print("1")
else:
    print("0")
