year = int(input())

counter = 0


while counter != 4:
    year += 1
    year = str(year)
    counter = 0

    for i in range(10):
        if str(i) in year:
            counter += 1
    year = int(year)

print(year)
