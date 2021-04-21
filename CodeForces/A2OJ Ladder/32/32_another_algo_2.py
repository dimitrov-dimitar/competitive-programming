# http://codeforces.com/problemset/problem/450/A


from math import ceil
n, m = map(int, input().split())
candies = [int(x) for x in input().split()]


max_num = 0
counter = 0
candies_dict = {}

for k in candies:
    counter += 1
    candies_dict[k] = counter


for i in candies:
    result = ceil(i / m)
    if result >= max_num:
        max_num = result
        max_candies = i

print(candies_dict[max_candies])
