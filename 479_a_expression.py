# https://codeforces.com/problemset/problem/479/A

a = int(input())
b = int(input())
c = int(input())

list_num = []

list_num.append((a + b * c))
list_num.append(((a + b) * c))
list_num.append((a * b * c))
list_num.append((a * b + c))
list_num.append((a * (b + c)))
list_num.append(a + b + c)

print(max(list_num))
