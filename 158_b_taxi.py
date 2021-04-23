# https://codeforces.com/problemset/problem/158/B

n = int(input())
s = [int(x) for x in input().split()]

sum_s = sum(s)
taxi = 0
# 3
# 3 3 2
# 3

s = sorted(s, reverse=True)

# for group in s:
#     if group == 4:
#         taxi += 1

four = s.count(4)
three = s.count(3)
two = s.count(2)
one = s.count(1)
