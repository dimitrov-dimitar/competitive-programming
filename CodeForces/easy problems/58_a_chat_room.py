# https://codeforces.com/problemset/problem/58/A

s = list(input())

word = ["h", "e", "l", "l", "o"]
counter = 0

for char in word:
    for letter in s:
        if char != letter:
            s = s[1:]
        else:
            s = s[1:]
            counter += 1
            break

if counter == 5:
    print("YES")
else:
    print("NO")
