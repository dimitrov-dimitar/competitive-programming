# https://codeforces.com/problemset/problem/4/C

from collections import Counter

n = int(input())
names = []


for x in range(n):
    text = input()
    names.append(text)

    number = names.count(text)
    if number == 1:
        print("OK")
    else:
        print(text + str(number - 1))
