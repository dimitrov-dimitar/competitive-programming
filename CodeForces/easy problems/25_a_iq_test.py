# https://codeforces.com/problemset/problem/25/A

n = int(input())
numbers = [int(x) for x in input().split()]

even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

if len(even) > len(odd):
    result = odd[0]
else:
    result = even[0]

print(numbers.index(result) + 1)
