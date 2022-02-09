# https://codeforces.com/problemset/problem/489/C

m, s = [int(x) for x in input().split()]

min_num = int("1" + ("0" * (m - 1)))
max_num = int("9" * m)

# first_num = -1
# last_num = -1


def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


if s > max_num or s < min_num:
    print(-1, -1)
else:

    for x in range(min_num, max_num + 1):
        if sum_digits(x) == s:
            first_num = x
            break

    for x in range(max_num, min_num - 1, -1):
        if sum_digits(x) == s:
            last_num = x
            break

    print(first_num, last_num)
