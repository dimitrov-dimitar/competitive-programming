# http://codeforces.com/problemset/problem/275/A

matrix_input = [list(map(int, input().split())) for i in range(3)]

x = 1
matrix_output = [[x for i in range(3)] for j in range(3)]

y = 0
matrix_sum = [[y for i in range(3)] for j in range(3)]

matrix_sum[0][0] = matrix_input[0][0] + matrix_input[0][1] + matrix_input[1][0]
matrix_sum[0][1] = matrix_input[0][1] + matrix_input[0][0] + matrix_input[0][2] + matrix_input[1][1]
matrix_sum[0][2] = matrix_input[0][2] + matrix_input[0][1] + matrix_input[1][2]
matrix_sum[1][0] = matrix_input[1][0] + matrix_input[0][0] + matrix_input[1][1] + matrix_input[2][0]
matrix_sum[1][1] = matrix_input[1][1] + matrix_input[0][1] + matrix_input[2][1] + matrix_input[1][0] + matrix_input[1][2]
matrix_sum[1][2] = matrix_input[1][2] + matrix_input[0][2] + matrix_input[2][2] + matrix_input[1][1]
matrix_sum[2][0] = matrix_input[2][0] + matrix_input[1][0] + matrix_input[2][1]
matrix_sum[2][1] = matrix_input[2][1] + matrix_input[1][1] + matrix_input[2][0] + matrix_input[2][2]
matrix_sum[2][2] = matrix_input[2][2] + matrix_input[1][2] + matrix_input[2][1]

# print(matrix_sum)

for row in range(3):
    for col in range(3):
        if matrix_sum[row][col] % 2 == 0:
            matrix_output[row][col] = 1
        else:
            matrix_output[row][col] = 0

for row in matrix_output:
    print("".join(map(str, row)))
