# https://codeforces.com/problemset/problem/116/A

n = int(input())

people_maximum = 0
tram = []


for i in range(n):
    passegengers = [int(x) for x in input().split()]
    people_exits = passegengers[0]
    people_enter = passegengers[1]
    people_maximum += people_enter - people_exits
    tram.append(people_maximum)

print(max(tram))
