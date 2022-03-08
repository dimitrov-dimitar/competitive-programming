# https://codeforces.com/problemset/problem/431/A

arr = [int(x) for x in input().split()]
s = input()

a1, a2, a3, a4 = arr
result = 0

result = (
    s.count("1") * a1
    + s.count("2") * a2
    + s.count("3") * a3
    + s.count("4") * a4
)

print(result)
