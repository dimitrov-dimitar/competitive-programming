# http://codeforces.com/problemset/problem/144/A

n = int(input())
soldiers_height = [int(x) for x in input().split()]

soldiers_height.reverse()
min_pos = len(soldiers_height) - soldiers_height.index(min(soldiers_height)) - 1

soldiers_height.reverse()
max_pos = soldiers_height.index(max(soldiers_height))

min_result = len(soldiers_height) - min_pos - 1
max_result = max_pos
# print(max_result, min_result)

if max_pos > min_pos:
    print(min_result + max_result - 1)
else:
    print(min_result + max_result)
