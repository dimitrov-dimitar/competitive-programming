n = 13
sum_counter = 1
max_counter = -1
max_n = 0

for n in range(1, 1000000):
    m = n
    while n != 1:

        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        #print(n, end= " ")
        sum_counter += 1
        if n == 1:
            break
    if sum_counter > max_counter:
        max_counter = sum_counter
        max_n = m

    sum_counter = 0
    #print()

print(max_n)