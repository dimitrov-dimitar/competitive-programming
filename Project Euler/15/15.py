array = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# array[0][0], array[2][2] = 1, 1
print(array)

sum_number = 0

for i in range(3):
    for j in range(3):
        if sum_number == 5:
            break
        if array[i][j] == 0:
            array[i][j] = 1
            sum_number += 1

print(array)
