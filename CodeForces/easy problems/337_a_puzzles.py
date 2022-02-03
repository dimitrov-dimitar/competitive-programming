# https://codeforces.com/problemset/problem/337/A

n, m = [int(x) for x in input().split()]
pieces = [int(x) for x in input().split()]

min_pieces = 99999999
pieces.sort()

if n == m:
    min_pieces = pieces[-1] - pieces[0]
    print(min_pieces)
else:
    for _ in range(m - n + 1):
        difference = pieces[n - 1] - pieces[0]
        if difference < min_pieces:
            min_pieces = difference
        pieces.pop(0)
    print(min_pieces)
