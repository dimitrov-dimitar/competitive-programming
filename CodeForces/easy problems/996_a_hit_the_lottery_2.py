# https://codeforces.com/problemset/problem/996/A

money = int(input())

coins = [1, 5, 10, 20, 100]
coins.reverse()
counter = 0

for coin in coins:
    if money >= coin:
        num = money // coin
        money -= num * coin
        counter += num

print(counter)
