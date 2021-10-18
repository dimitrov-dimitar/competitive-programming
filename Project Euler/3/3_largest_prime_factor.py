sum_counter = 0
# 600851475143
number = 600851475143

for i in range(2, 10000):
    for j in range(1, i + 1):
        if i % j == 0:
            sum_counter += 1

    if sum_counter == 2:
        # print(i, end= " ")
        if number % i == 0:
            print()
            print(f"prime factors for {number} : {i}", end=" ")
            print()

    sum_counter = 0

print()
