import time, sys
start_time = time.time()

positive_inf = float('inf')

sum_counter = 0
prime_position = 0

for i in range(2, sys.maxsize):
    for j in range(1, i + 1):
        if i % j == 0:
            sum_counter += 1

    if sum_counter == 2:
        prime_position += 1
        #print(f"prime position {prime_position} -> {i}")
        if prime_position == 10001:
            print(f"position {prime_position} -> {i}")
            break
    sum_counter = 0

print("Finish")

print("--- %s seconds ---" % (time.time() - start_time))

time = (time.time() - start_time)
time = int(time)
print(f"{time // 60}min {time % 60}sec")