# https://codeforces.com/problemset/problem/1512/A

t = int(input())

for _ in range(t):
    n = int(input())
    n_array = [int(x) for x in input().split()]

    for x in range(0, len(n_array)):
        if n_array[x] == n_array[x + 1]:
            equal_num = n_array[x]
            pass
        else:
            if n_array.count(n_array[x]) == 1:
                finding_num = n_array[x]
            else:
                finding_num = n_array[x + 1]
            print(n_array.index(finding_num) + 1)
            break
