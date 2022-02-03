# https://codeforces.com/problemset/problem/230/A


s, n = [int(x) for x in input().split()]
dragons = []
new_dragons = []

for _ in range(n):
    x, y = [int(x) for x in input().split()]
    dragons.append([x, y])

dragons.sort()

for row in range(n - 1):
    current_row = dragons[row]
    next_row = dragons[row + 1]
    if current_row[0] == next_row[0]:
        if current_row[1] < next_row[1]:
            dragons[row], dragons[row + 1] = dragons[row + 1], dragons[row]
        else:
            continue

# print(dragons)

bool_var = True

for row in dragons:
    if s > row[0]:
        s += row[1]

    else:
        print("NO")
        bool_var = False
        break

if bool_var:
    print("YES")
