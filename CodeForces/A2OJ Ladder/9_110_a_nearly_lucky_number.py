# http://codeforces.com/problemset/problem/110/A

number = input()

counter = 0

for digit in number:
    if digit == "4" or digit == "7":
        counter += 1

if counter == 4 or counter == 7:
    print("YES")
else:
    print("NO")
