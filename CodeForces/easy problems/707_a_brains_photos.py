# https://codeforces.com/problemset/problem/707/A

n, m = [int(x) for x in input().split()]
array = []

for row in range(n):
    array.append([x for x in input().split()])

color_str = ""

for r in range(n):
    for c in range(m):
        color_str += array[r][c]

if (
    color_str.count("C") == 0
    and color_str.count("M") == 0
    and color_str.count("Y") == 0
):
    print("#Black&White")
else:
    print("#Color")
