first_n = 0
second_n = 1
number = 0
sum_number = 0


#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

for i in range(1, 100):

    number = first_n + second_n
    first_n = second_n
    second_n = number
    #print(number, end= " ")
    if number % 2 == 0:
        sum_number += number
        if 4000000 < sum_number < 5000000:
            print(sum_number, end= " ")


print("Finish")