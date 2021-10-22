# number = 2520

# for i in range(1, 11):
#     if number % i == 0:
#         print(f"{number} % {i} == 0")

import time

start_time = time.time()
sum_counter = 0
is_bool = True


for i in range(200000000, 300000000):
    for j in range(1, 21):
        if i % j == 0:
            sum_counter += 1

        if sum_counter == 20:
            print(f"{i}")
            is_bool = False
            break

    sum_counter = 0
    if not is_bool:
        break

print("Finish")
print("--- %s seconds ---" % (time.time() - start_time))
