# https://codeforces.com/problemset/problem/486/A

import math

n = int(input())

result = 0

# time complexity
# for num in range(1, n + 1):
#     if num % 2 != 0:
#         result -= num
#     else:
#         result += num

# print(result)

result = math.ceil(n / 2)

if n % 2 != 0:
    result *= -1

print(result)
