# https://codeforces.com/problemset/problem/133/A

p = input()

programming_lang = ["H", "Q", "9"]
counter = 0

for i in programming_lang:
    if i in p:
        counter += 1

if counter > 0:
    print("YES")
else:
    print("NO")
