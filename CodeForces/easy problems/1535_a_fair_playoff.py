# https://codeforces.com/problemset/problem/1535/A

import copy

t = int(input())

for _ in range(t):
    s_players = [int(x) for x in input().split()]
    copy_s_players = copy.copy(s_players)
    copy_s_players.sort()

    max_one = copy_s_players[-2]
    max_two = copy_s_players[-1]
    temp_arr = []

    while s_players:
        first = s_players[0]
        second = s_players[1]

        temp_arr.append(max(first, second))

        s_players.remove(first)
        s_players.remove(second)

    # print(temp_arr)
    # if max_one in temp_arr and max_two in temp_arr:
    if all(x in temp_arr for x in [max_one, max_two]):
        print("YES")
    else:
        print("NO")
