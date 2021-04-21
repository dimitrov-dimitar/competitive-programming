# http://codeforces.com/problemset/problem/61/A

first_n = input()
second_n = input()

result = ""

for digit in range(len(first_n)):
    if first_n[digit] != second_n[digit]:
        result += "1"
    else:
        result += "0"

print(result)
