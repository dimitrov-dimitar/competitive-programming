# https://codeforces.com/problemset/problem/1374/B

t = int(input())
counter = 0
multiply_counter = 0

for _ in range(t):
    n = int(input())

    while True:
        if multiply_counter > 3:
            print(-1)
            break
        if n == 1:
            print(counter)
            break
        if n % 6 == 0:
            n /= 6
            counter += 1
            multiply_counter = 0
        else:
            n *= 2
            counter += 1
            multiply_counter += 1

    counter = 0
    multiply_counter = 0
