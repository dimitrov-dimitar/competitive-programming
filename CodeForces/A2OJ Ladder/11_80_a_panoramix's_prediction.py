digits_input = input().split()

n = int(digits_input[0])
m = int(digits_input[1])

k = n + 1
counter = 0

while counter != 1:
    counter = 0
    for i in range(k, 1, -1):
        if k % i == 0:
            counter += 1
            if counter > 1:
                k += 1
                break

if m == k:
    print("YES")
else:
    print("NO")
