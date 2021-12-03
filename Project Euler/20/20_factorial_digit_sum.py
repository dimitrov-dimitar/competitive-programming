# 100! calc and sum all digits in it

from math import factorial

n = 100
multiplication_i = 1
sum_digits = 0

for i in range(n, 1, -1):
    multiplication_i *= i
print(multiplication_i)

# print(factorial(n))


multiplication_i = str(multiplication_i)

for digits in multiplication_i:
    sum_digits += int(digits)
print(sum_digits)


# another way
print(sum(map(int, str(multiplication_i))))
