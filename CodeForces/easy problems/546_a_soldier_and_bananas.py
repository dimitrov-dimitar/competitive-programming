# https://codeforces.com/problemset/problem/546/A

k, n, w = [int(x) for x in input().split()]

# w - bananas, k - dollars for first banana, n - total money
money_spend = 0

for number in range(1, w + 1):
    money_spend += number * k

borrow_money = n - money_spend

if borrow_money < 0:
    print(abs(borrow_money))
else:
    print(0)
