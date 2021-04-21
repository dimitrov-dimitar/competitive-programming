# http://codeforces.com/problemset/problem/69/A

n = int(input())
list_sum = [0, 0, 0]

for row in range(n):
    coordinates = input().split()
    x = int(coordinates[0])
    y = int(coordinates[1])
    z = int(coordinates[2])
    list_sum[0] += x
    list_sum[1] += y
    list_sum[2] += z

if list_sum[0] == 0 and list_sum[1] == 0 and list_sum[2] == 0:
    print("YES")
else:
    print("NO")
