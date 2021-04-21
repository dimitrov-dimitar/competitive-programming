n = int(input())
points = [int(x) for x in input().split()]

min_points = points[0]
max_points = points[0]
counter = 0


for result in range(1, len(points)):
    if points[result] < min_points:
        counter += 1
        min_points = points[result]

    if points[result] > max_points:
        counter += 1
        max_points = points[result]

print(counter)
