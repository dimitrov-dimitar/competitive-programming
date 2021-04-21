numbers = [int(x) for x in input().split()]

counter = 0

for i in range(0, len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            numbers.pop(i + 1)
            counter += 1

print(counter)
