# https://codeforces.com/problemset/problem/160/A

n = int(input())
coins_value = list(map(int, input().split()))
coins_value = sorted(coins_value, reverse=True)

sum_coins = sum(coins_value)
number_coins = 0


break_var = True
mine_coins = 0

while True:
    if n == 1:
        number_coins = 1
        break
    if break_var:
        number_coins += 1
        mine_coins += coins_value.pop(0)
        if mine_coins > sum(coins_value):
            break_var = False
            break

print(number_coins)
# print(mine_coins)
