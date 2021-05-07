# https://codeforces.com/problemset/problem/1328/A

t = int(input())

# counter = 0

for _ in range(t):
    a, b = [int(x) for x in input().split()]
    # while a % b != 0:
    #     a += 1
    #     counter += 1
    # print(counter)
    # counter = 0

    if a % b == 0:
        print(0)
    print(a % b)
