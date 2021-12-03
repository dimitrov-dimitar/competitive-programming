import time

start_time = time.time()

positive_inf = float("inf")
i = 2
j = 1
sum_counter = 0
prime_position = 0

while i < positive_inf:
    while j <= i:
        if i % j == 0:
            sum_counter += 1
        j += 1
    if sum_counter == 2:
        prime_position += 1
        # print(f"prime position {prime_position} -> {i}")
        if prime_position == 10001:
            print(f"position {prime_position} -> {i}")
            break
    sum_counter = 0
    i += 1
    j = 1
print("Finish")
print("--- %s seconds ---" % (time.time() - start_time))
