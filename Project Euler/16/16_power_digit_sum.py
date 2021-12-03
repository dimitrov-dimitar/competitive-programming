n = 2 ** 1000
sum_counter = 0

print(n)
print(len(str(n)))

n = str(n)
# print(n[0])

for i in range(len(n)):
    # print(n[i])
    sum_counter += int(n[i])

print(sum_counter)
