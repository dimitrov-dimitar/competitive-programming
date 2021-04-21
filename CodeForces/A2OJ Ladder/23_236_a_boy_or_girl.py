# https://codeforces.com/problemset/problem/236/A

string = input()

result = "".join(set(string))

if len(result) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
