# https://codeforces.com/problemset/problem/268/A

n = int(input())

games = n * (n - 1)
teams_h = []
teams_a = []
counter = 0

for _ in range(n):
    h, a = [int(x) for x in input().split()]
    teams_h.append(h)
    teams_a.append(a)


# print(teams_h, teams_a)

for h in range(n):
    for a in range(n):
        if teams_h[h] == teams_a[a]:
            counter += 1

print(counter)
