# https://codeforces.com/problemset/problem/4/C


n = int(input())
names = {}


for x in range(n):
    text = input()
    if text not in names:
        names[text] = 0
        print("OK")
    else:
        names[text] += 1
        print(text + str(names[text]))
