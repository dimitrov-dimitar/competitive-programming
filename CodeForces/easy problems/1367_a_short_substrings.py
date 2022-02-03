# https://codeforces.com/problemset/problem/1367/A

t = int(input())

list_a = []

for _ in range(t):
    b = input()
    if len(b) == 2:
        print(b)
        continue
    else:
        for n in range(0, len(b), 2):
            list_a.append(b[n])
        list_a.append(b[-1])
    print("".join(list_a))
    list_a = []
