import time
start_time = time.time()

sum_counter = 0
sum_prime = 0

for i in range(1, 100000):
    for j in range(1, i + 1):
        if i % j == 0:
            sum_counter += 1
            if sum_counter > 2:
                break
    if sum_counter == 2:
        print(i)
        sum_prime += i

    sum_counter = 0

print(sum_prime)
print("Finish")

time = (time.time() - start_time)
time = int(time)
print(f"{time // 60}min {time % 60}sec")