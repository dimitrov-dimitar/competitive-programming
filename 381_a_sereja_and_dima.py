# https://codeforces.com/problemset/problem/381/A

n = int(input())
cards = [int(x) for x in input().split()]

s_arr = []
d_arr = []

for i in range(n):
    if i % 2 == 0:
        s_arr.append(cards.pop(cards.index(max(cards[0], cards[-1]))))
    else:
        d_arr.append(cards.pop(cards.index(max(cards[0], cards[-1]))))

print(sum(s_arr), sum(d_arr))
