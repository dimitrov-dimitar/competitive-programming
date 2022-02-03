# https://codeforces.com/problemset/problem/1399/A

t = int(input())

for _ in range(t):
    length_a = int(input())
    list_a = [int(x) for x in input().split()]
    list_a.sort()
    while True:
        if len(list_a) == 1:
            print("YES")
            break
        elif abs(list_a[0] - list_a[1]) <= 1:
            list_a.pop(0)
        else:
            print("NO")
            break
