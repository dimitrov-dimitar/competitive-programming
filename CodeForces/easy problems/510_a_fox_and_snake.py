# https://codeforces.com/problemset/problem/510/A

n, m = [int(x) for x in input().split()]

counter = 0

for row in range(1, n + 1):
    if row % 2 == 1:
        print(m * "#")
    else:
        counter += 1
        if counter % 2 == 1:
            print((m - 1) * "." + "#")
        else:
            print("#" + (m - 1) * ".")
