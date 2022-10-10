# https://codeforces.com/problemset/problem/200/B

n = int(input())
nums = [int(x) for x in input().split()]

result = sum(nums) / n
print(result)
