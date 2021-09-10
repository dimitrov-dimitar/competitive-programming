# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
n = 1
sum_counter = 0
i = 2
j = 1

while i < 100:
    
    #print(n)
    while j <= n:
        if n % j == 0:
            sum_counter += 1
        j += 1
        
    print(f"{n} -> {j - 1}, {sum_counter}")

    # if sum_counter > 300:
    #     print(f"{n} -> {j}, {sum_counter}")

    # if sum_counter > 400:
    #     print(f"{n} -> {j}, {sum_counter}")

    # if sum_counter > 500:
    #     print(f"{n} -> {j}, {sum_counter}")
    #     break
    j = 1    
    sum_counter = 0 
    n += i
    i += 1
