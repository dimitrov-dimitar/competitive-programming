numbers = input().split()

children = int(numbers[0])
time = int(numbers[1])

# s = list(input())
s = [char for char in input()]


for j in range(time):

    i = 0
    while i < len(s) - 1:
        if s[i] == "B" and s[i+1] == "G":
            s[i], s[i+1] = s[i+1], s[i]
            i += 2
        else:
            i += 1
print("".join(s))
