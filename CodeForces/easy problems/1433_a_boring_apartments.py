# https://codeforces.com/problemset/problem/1433/A

t = int(input())

l_num = [1, 2, 3, 4]
counter = 0

for _ in range(t):
    x = input()
    first_digit = int(x[0])
    counter = (first_digit - 1) * sum(l_num) + sum(l_num[: len(x)])
    print(counter)
    counter = 0
