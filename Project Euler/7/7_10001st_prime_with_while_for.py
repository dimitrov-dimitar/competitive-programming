positive_inf = float('inf')
i = 0
sum_counter = 0
prime_position = 0

while i < positive_inf:
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
    i += 1

print("Finish")