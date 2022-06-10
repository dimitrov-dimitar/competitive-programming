# https://leetcode.com/problems/fizz-buzz/

n = int(input())

fizz_buzz = []

for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        fizz_buzz.append("FizzBuzz")
    elif i % 3 == 0:
        fizz_buzz.append("Fizz")
    elif i % 5 == 0:
        fizz_buzz.append("Buzz")
    else:
        fizz_buzz.append(str(i))


print(fizz_buzz)
