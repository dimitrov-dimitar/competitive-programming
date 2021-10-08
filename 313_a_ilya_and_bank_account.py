# https://codeforces.com/problemset/problem/313/A

n = int(input())

if n >= 0:
    print(n)
else:
    # last = abs(n) % 10
    last = str(n)[-1]
    prev = str(n)[-2]

    new_num = str(n)
    if last >= prev:
        new_num = new_num[:-1]
    else:
        new_num = new_num[:-2] + last
    print(int(new_num))
