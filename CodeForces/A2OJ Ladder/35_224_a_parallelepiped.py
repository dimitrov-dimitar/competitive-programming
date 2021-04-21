# http://codeforces.com/problemset/problem/224/A

from math import sqrt


s1, s2, s3 = map(int, input().split())

a = sqrt((s1 * s3) / s2)
b = sqrt((s1 * s2) / s3)
c = sqrt((s2 * s3) / s1)

result = 4 * (a + b + c)
print(int(result))
