# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
n = 1
sum_counter = 0

for i in range(2, 100):
    
    #print(n)
    for j in range(1, n + 1):
        if n % j == 0:
            sum_counter += 1
            print(f"{n} -> {j}, {sum_counter}")

            if sum_counter > 300:
                print(f"{n} -> {j}, {sum_counter}")

            if sum_counter > 400:
                print(f"{n} -> {j}, {sum_counter}")

            if sum_counter > 500:
                print(f"{n} -> {j}, {sum_counter}")
                break

        
    sum_counter = 0 
    
    n += i

