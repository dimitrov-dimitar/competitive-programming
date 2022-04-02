# https://codeforces.com/problemset/problem/9/A

y, w = [int(x) for x in input().split()]

max_num = max(y, w)

if max_num == 1:
    print("1/1")
elif max_num == 2:
    print("5/6")
elif max_num == 3:
    print("2/3")
elif max_num == 4:
    print("1/2")
elif max_num == 5:
    print("1/3")
else:
    print("1/6")
