# http://codeforces.com/problemset/problem/450/A


# n, m = [int(x) for x in input().split()]
n, m = map(int, input().split())
candies = [int(x) for x in input().split()]

children = [int(x) for x in range(1, n + 1)]
max_child = -99

for child in children:
    if child > max_child:
        max_child = child
        
