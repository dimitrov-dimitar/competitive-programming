# https://codeforces.com/problemset/problem/230/B

n = int(input())
numbers = [int(x) for x in input().split()]

counter = 0

for number in numbers:
    if number == 1 or number == 2:
        print("NO")
        continue
    for x in range(2, number):
        if counter > 1:
            break
        if number % x == 0:
            counter += 1
    if counter == 1:
        print("YES")
    else:
        print("NO")
    counter = 0
