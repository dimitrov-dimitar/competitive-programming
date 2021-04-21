# http://codeforces.com/problemset/problem/231/A

n = int(input())

counter = 0

for _ in range(n):
    solution = []
    solution = [int(x) for x in input().split()]
    if sum(solution) > 1:
        counter += 1

print(counter)
