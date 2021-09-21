# https://codeforces.com/problemset/problem/723/A

friends = [int(x) for x in input().split()]

result = max(friends) - min(friends)

print(result)
