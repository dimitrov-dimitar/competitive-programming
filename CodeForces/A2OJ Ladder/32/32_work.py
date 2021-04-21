# http://codeforces.com/problemset/problem/450/A

from collections import deque

# n, m = [int(x) for x in input().split()]
n, m = map(int, input().split())
candies = [int(x) for x in input().split()]

children = deque([int(x) for x in range(1, n + 1)])
home = []

while True:
    if len(home) == n:
        break
    for i in range(len(children)):
        child = children.popleft()
        if m >= candies[i]:
            home.append(child)
        else:
            children.append(child)

print(home[-1])
