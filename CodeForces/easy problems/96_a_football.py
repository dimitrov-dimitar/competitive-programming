# https://codeforces.com/problemset/problem/96/A

text = input()

counter_0 = 1
counter_1 = 1
same = ""
true_var = False


for char in text:
    if char == "0":
        counter_0 += 1
    else:
        counter_1 += 1

    if counter_0 == 7 or counter_1 == 7:
        true_var = True
        break

    if char != same:
        counter_0 = 1
        counter_1 = 1
        same = char

# print(counter_0, counter_1)

if true_var:
    print("YES")
else:
    print("NO")
