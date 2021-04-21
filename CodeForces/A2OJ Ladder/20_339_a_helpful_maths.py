# https://codeforces.com/problemset/problem/339/A

s = [x for x in input().split("+")]

if len(s) == 1:
    print(s[0])
else:
    s.sort()
    print("+".join(s))
