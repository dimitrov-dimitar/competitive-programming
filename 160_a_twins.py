# https://codeforces.com/problemset/problem/160/A

n = int(input())
coins_value = list(map(int, input().split()))

sum_coins = sum(coins_value)
number_coins = 0

if n == 1:
    number_coins = 1

print(number_coins)
