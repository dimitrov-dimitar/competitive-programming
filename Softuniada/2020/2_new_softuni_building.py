n = int(input())

height = int(n + n / 2)
seats = '#'
empty_space = '.'


for row in range(height):
    for col in range(n):
        stripe = (col + row) % 4 == 0
        if stripe:
            print(seats, end='')
        else:
            print(empty_space, end='')
    print()
