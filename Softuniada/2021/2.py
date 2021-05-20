n = int(input())

empty = ' '


def row_calc(number):
    for em in range(n - row):
        print(empty, end='')
    for num in range(1, number):
        print(num, end='')
    for num in range(number, 0, -1):
        print(num, end='')
    for em in range(n - row):
        print(empty, end='')
    print()


for row in range(n, 0, -1):
    row_calc(row)
