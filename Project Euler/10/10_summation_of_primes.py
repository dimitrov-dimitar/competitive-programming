import time

start_time = time.time()

sum_prime = 0

for i in range(2, 2000000):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        #print(i)              
        sum_prime += i

print(sum_prime)
print("Finish")

time = (time.time() - start_time)
time = int(time)
print(f"{time // 60}min {time % 60}sec")