for num in range(1, n + 1):
    if num % 2 != 0:
        result -= num
    else:
        result += num

print(result)
