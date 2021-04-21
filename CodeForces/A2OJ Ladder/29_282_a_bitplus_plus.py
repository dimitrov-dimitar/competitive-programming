# http://codeforces.com/problemset/problem/282/A

n = int(input())

counter = 0

for _ in range(n):
    statement = input()
    if "+" in statement:
        counter += 1
    elif "-" in statement:
        counter -= 1

print(counter)
