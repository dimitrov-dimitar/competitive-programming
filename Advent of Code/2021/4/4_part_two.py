# Part Two


def bingo(grid):
    for row in grid:
        if all([element == "X" for element in row]):
            return True
    for num in range(len(grid[0])):
        column = [row[num] for row in grid]
        if all([element == "X" for element in column]):
            return True


matrix = []

with open("input2") as f:
    for row in f:
        row = row.rstrip("\n")
        matrix.append(row)

_, rest = (matrix[0], matrix[1:])

numbers = [int(x) for x in matrix[0].split(",")]
rest = [" ".join(x.split()) for x in rest]

new_list = list(filter(None, rest))

new_list = [row.split() for row in new_list]
new_list = [[int(x) for x in row] for row in new_list]
break_var = False

while True:
    if break_var:
        break
    for number in numbers:
        if break_var:
            break
        n = 0
        k = 5
        while k <= len(new_list):
            grid = new_list[n:k]
            original_grid = grid

            for row in range(5):
                for el in range(5):
                    if grid[row][el] == number:
                        grid[row][el] = "X"

            if bingo(grid):
                # print(original_grid)
                # print(grid)
                # print(number)
                total = 0
                sum_numbers = [
                    [total := total + x for x in row if type(x) != str] for row in grid
                ]
                result = total * number
                print(result)
                break

            n += 5
            k += 5


print("done")
