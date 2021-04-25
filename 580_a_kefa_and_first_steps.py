# https://codeforces.com/problemset/problem/580/A

n = int(input())
money = [int(x) for x in input().split()]

counter = 1
max_counter = 0

for num in range(n - 1):
    current = money[num]
    next_num = money[num + 1]
    if next_num >= current:
        counter += 1
    else:
        counter = 1

    if counter > max_counter:
        max_counter = counter

if n == 1:
    max_counter = 1

print(max_counter)
