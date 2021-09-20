# https://codeforces.com/problemset/problem/432/A

n, k = [int(x) for x in input().split()]
perticipated = [int(x) for x in input().split()]

perticipated = sorted(perticipated)
max_teams = n // 3
team = []
counter = 0


for _ in range(max_teams):
    team = perticipated[:3]
    team = [x + k for x in team]
    # print(perticipated)
    if any(x > 5 for x in team):
        continue
    else:
        counter += 1
    perticipated = perticipated[3:]

print(counter)
