# http://codeforces.com/problemset/problem/266/A

n = int(input())
s = input()

counter = 0

for i in range(n - 1):
    if s[i] == s[i+1]:
        counter += 1

print(counter)
