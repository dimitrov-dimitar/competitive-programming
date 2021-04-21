# http://codeforces.com/problemset/problem/148/A

k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

dragons = [x for x in range(1, d + 1)]
dragons_damaged = []

for dragon in range(d):
    if dragons[dragon] == 0:
        continue
    else:
        if dragons[dragon] % k == 0:
            dragons_damaged.append(dragons[dragon])
            dragons[dragon] = 0

for dragon in range(d):
    if dragons[dragon] == 0:
        continue
    else:
        if dragons[dragon] % l == 0:
            dragons_damaged.append(dragons[dragon])
            dragons[dragon] = 0

for dragon in range(d):
    if dragons[dragon] == 0:
        continue
    else:
        if dragons[dragon] % m == 0:
            dragons_damaged.append(dragons[dragon])
            dragons[dragon] = 0
for dragon in range(d):
    if dragons[dragon] == 0:
        continue
    else:
        if dragons[dragon] % n == 0:
            dragons_damaged.append(dragons[dragon])
            dragons[dragon] = 0

# print(dragons)
# print(dragons_damaged)
print(len(dragons_damaged))
