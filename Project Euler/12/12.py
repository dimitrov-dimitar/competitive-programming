number = 0
sum_counter = 0


for i in range(1, 10000000):

    number = i * (i + 1) / 2
    #print(number)
    for j in range(1, int(number + 1)):
        if number % j == 0:
            sum_counter += 1

    if sum_counter > 300:
        print(number, sum_counter)
    if sum_counter > 400:
        print(number)
    if sum_counter > 500:
        print(number)
        break

    sum_counter = 0
    