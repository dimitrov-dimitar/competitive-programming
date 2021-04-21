# https://codeforces.com/problemset/problem/233/A

n = int(input())

elements = [x for x in range(1, n+1)]


if n % 2 == 0:
    for i in range(0, n, 2):
        elements[i], elements[i+1] = elements[i+1], elements[i]
    elements = [str(x) for x in elements]
    print(" ".join(elements))
else:
    print(-1)
