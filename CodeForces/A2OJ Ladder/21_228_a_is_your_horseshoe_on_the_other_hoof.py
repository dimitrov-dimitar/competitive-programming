# https://codeforces.com/problemset/problem/228/A

numbers = [int(x) for x in input().split()]
numbers_copy = numbers.copy()

counter = 0

for i in numbers:
    numbers_copy.remove(i)
    if i in numbers_copy:
        counter += 1

print(counter)
