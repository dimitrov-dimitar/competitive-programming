n = float(input())
m = float(input())
x = float(input())
y = float(input())
t = int(input())

sum_money = 0
money_spend = 0

for i in range(t):
    sum_money += n
    n += x
money_spend = t * m

total_money = sum_money - money_spend

if total_money >= y:
    print("Have a nice ride!")
else:
    print("Work harder!")
