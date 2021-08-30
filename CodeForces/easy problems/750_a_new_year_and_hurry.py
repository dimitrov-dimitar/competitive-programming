n, m = [int(x) for x in input().split()]

minutes_counter = 0
total_min = 240
free_time = total_min - m
counter = 0


for problem in range(1, n + 1):
    free_time -= problem * 5
    if free_time >= 0:
        counter += 1

print(counter)
