# https://codeforces.com/problemset/problem/1385/A

t = int(input())

for _ in range(t):
    num_arr = []
    x, y, z = [int(x) for x in input().split()]
    num_arr.append(x)
    num_arr.append(y)
    num_arr.append(z)
    num_arr.sort()

    if x == y == z:
        print("YES")
        print(x, y, z)

    elif num_arr[0] < num_arr[1] and num_arr[1] == num_arr[2]:
        print("YES")
        print(num_arr[0], num_arr[0], num_arr[1])

    else:
        print("NO")
