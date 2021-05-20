n = int(input())
m = int(input())

prime_numbers = []

for i in range(n, m + 1):
    if i > 1:
        for j in range(2, i):
            if (i % j == 0):
                break
        else:
            prime_numbers.append(i)

for num in prime_numbers:
    print(num, end=' ')

print()
print(f'The total number of prime numbers between {n} to {m} is {len(prime_numbers)}')
