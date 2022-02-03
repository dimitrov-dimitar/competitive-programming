# https://codeforces.com/problemset/problem/136/A

n = int(input())

friends = [int(x) for x in input().split()]

result = {}


for count, value in enumerate(friends):
    result[value] = count + 1

result = dict(sorted(result.items()))

for v in result.values():
    print(v, end=" ")
