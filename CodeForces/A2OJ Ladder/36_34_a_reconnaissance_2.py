# http://codeforces.com/problemset/problem/34/A

n = int(input())
heights = [int(x) for x in input().split()]

soldiers = [x for x in range(1, n + 1)]

heights.append(heights[0])
soldiers.append(soldiers[0])

first_min = 0
second_min = 0
difference_min = 999999999999999999999999

for i in range(len(heights) - 1):
    difference = abs(heights[i] - heights[i+1])
    if difference < difference_min:
        difference_min = difference
        first_min = soldiers[i]
        second_min = soldiers[i+1]

print(first_min, second_min)
