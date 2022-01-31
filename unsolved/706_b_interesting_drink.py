# https://codeforces.com/problemset/problem/706/B

n = int(input())
n_array = [int(x) for x in input().split()]
q = int(input())

q_array = []
counter = 0

for x in range(q):
    num = int(input())
    q_array.append(num)

n_array.sort()

for shop in q_array:
    if len(n_array) == 1:
        if shop > n_array[0]:
            print(1)
        else:
            print(0)

    else:
        mid = len(n_array) // 2
        if shop > n_array[mid]:
            for x in range(mid, len(n_array)):
                if shop < n_array[x]:
                    print(x)
                    break
                if x == len(n_array) - 1:
                    print(len(n_array))
        else:
            for x in range(mid - 1, -1, -1):
                if shop >= n_array[x]:
                    print(x + 1)
                    break
                if x == 0:
                    print(0)
