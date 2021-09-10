k = 0
max_number = -99999999999


for i in reversed(range(900, 1000)):
    for j in reversed(range(900, 1000)):
        k = i * j
        k = str(k)
        if len(k) == 6:
            if k[0] == k[5] and k[1] == k[4] and k[2] == k[3]:
                print(f"k = i * j -> {k} = {i} * {j} ")
                k = int(k)
                if k > max_number:
                    max_number = k

print(max_number)