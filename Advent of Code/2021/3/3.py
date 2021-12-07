# Part One
matrix = []

with open("input") as f:
    for row in f:
        matrix.append(row)

gama_rate = ""
epsilon_rate = ""
element_list = []


def most_frequent(List):
    return max(set(List), key=List.count)


l_row = int(len(matrix[0]))

for el in range(1, l_row):
    for row in matrix:
        element = row[el - 1]
        element_list.append(int(element))

    most_fr = str(most_frequent(element_list))
    gama_rate += most_fr
    if most_fr == "1":
        epsilon_rate += "0"
    else:
        epsilon_rate += "1"
    element_list = []


gama_rate_decimal = int(gama_rate, 2)
epsilon_rate_decimal = int(epsilon_rate, 2)

print(gama_rate_decimal * epsilon_rate_decimal)


# Part One
list_ones = []
list_zeroes = []
counter = 0
original_matrix = matrix

while len(matrix) != 1:
    for row in matrix:
        if row[counter] == '0':
            list_zeroes.append(row)
        else:
            list_ones.append(row)

    if len(list_zeroes) > len(list_ones):
        list_ones = []
        matrix = list_zeroes
        list_zeroes = []
    elif len(list_ones) > len(list_zeroes):
        list_zeroes = []
        matrix = list_ones
        list_ones = []
    else:
        list_zeroes = []
        matrix = list_ones
        list_ones = []

    counter += 1

oxygen_generator = matrix[0]
# print(oxygen_generator)

list_ones = []
list_zeroes = []
counter = 0
matrix = original_matrix

while len(matrix) != 1:
    for row in matrix:
        if row[counter] == '0':
            list_zeroes.append(row)
        else:
            list_ones.append(row)

    if len(list_zeroes) < len(list_ones):
        list_ones = []
        matrix = list_zeroes
        list_zeroes = []
    elif len(list_ones) < len(list_zeroes):
        list_zeroes = []
        matrix = list_ones
        list_ones = []
    else:
        list_ones = []
        matrix = list_zeroes
        list_zeroes = []

    counter += 1

co2_scrubber = matrix[0]
# print(co2_scrubber)

oxygen_generator_decimal = int(oxygen_generator, 2)
co2_scrubber_decimal = int(co2_scrubber, 2)

print(oxygen_generator_decimal * co2_scrubber_decimal)
