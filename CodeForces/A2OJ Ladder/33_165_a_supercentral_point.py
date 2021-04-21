# http://codeforces.com/problemset/problem/165/A

import copy
n = int(input())

points = []
counter = 0


for _ in range(n):
    points.append(tuple(int(x) for x in input().split()))

points_copy = copy.copy(points)
# print(points)


def right_neighbor():
    for x1, y1 in points_copy:
        if x1 > x and y1 == y:
            return True


def left_neighbor():
    for x1, y1 in points_copy:
        if x1 < x and y1 == y:
            return True


def lower_neighbor():
    for x1, y1 in points_copy:
        if x1 == x and y1 < y:
            return True


def upper_neighbor():
    for x1, y1 in points_copy:
        if x1 == x and y1 > y:
            return True


for point in points:
    x, y = point
    points_copy.remove(point)

    if right_neighbor() and left_neighbor() and lower_neighbor() and upper_neighbor():
        counter += 1
    points_copy.append(point)

print(counter)
