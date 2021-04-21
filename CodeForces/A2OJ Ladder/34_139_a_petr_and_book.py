# http://codeforces.com/problemset/problem/139/A

n = int(input())
# days_reading = list(map(int, input().split()))
days_reading = [int(x) for x in input().split()]

counter = 0

# print(days_reading)

while n > 0:
    counter = 0
    for day in days_reading:
        n -= day
        counter += 1
        if n <= 0:
            last_day = counter
            break
    # n -= 1

print(last_day)
