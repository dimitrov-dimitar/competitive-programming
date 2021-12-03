# a = 3
# b = 4
# c = 5

# if a ** 2 + b ** 2 == c ** 2:
#     print(f"{a} ** 2 + {b} ** 2 = {c} ** 2")


for i in range(3, 1000):
    for j in range(4, 1000):
        for k in range(5, 1000):
            if i ** 2 + j ** 2 == k ** 2:
                # print(f"{i} + {j} = {k}")
                if i + j + k == 1000:
                    print(f"{i}, {j}, {k}")
                    print(i * j * k)
                    break
        else:
            continue
        break
    else:
        continue
    break

print("Finish")
