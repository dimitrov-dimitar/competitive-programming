# https://codeforces.com/problemset/problem/1409/A

t = int(input())
list_diff = []

for _ in range(t):
    a, b = [int(x) for x in input().split()]
    diff = abs(a - b)
    last_digit = diff % 10
    result = diff // 10

    if last_digit != 0:
        result += 1
    list_diff.append(result)

for num in list_diff:
    print(num)
