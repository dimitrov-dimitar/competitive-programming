sum_square = 0
square_sum = 0


for i in range(1, 101):
    sum_square += i

sum_square **=  2

for j in range(1, 101):
    j **= 2
    square_sum += j

print(sum_square - square_sum)