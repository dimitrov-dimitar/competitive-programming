# http://codeforces.com/problemset/problem/200/B

n = int(input())
elements = [int(x) for x in input().split()]

result = sum(elements) / n
print(f"{result:.12f}")
