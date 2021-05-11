# https://codeforces.com/problemset/problem/996/A

money = int(input())

dollar_bills = 0

# pypy3

while money >= 100:
    money -= 100
    dollar_bills += 1

while money >= 20:
    money -= 20
    dollar_bills += 1

while money >= 10:
    money -= 10
    dollar_bills += 1

while money >= 5:
    money -= 5
    dollar_bills += 1

while money >= 1:
    money -= 1
    dollar_bills += 1


print(dollar_bills)
