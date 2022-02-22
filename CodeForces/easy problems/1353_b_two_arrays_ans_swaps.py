# https://codeforces.com/problemset/problem/1353/B

t = int(input())

for _ in range(t):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    for _ in range(k):
        min_num_a = min(a)
        max_num_b = max(b)

        if min_num_a < max_num_b:
            a.remove(min_num_a)
            b.remove(max_num_b)

            a.append(max_num_b)
            b.append(min_num_a)

    print(sum(a))
