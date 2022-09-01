# https://codeforces.com/problemset/problem/977/B

n = int(input())
s = input()

alpha_dict = {}

for i in range(len(s) - 1):
    current = s[i]
    next = s[i + 1]
    key = current + next
    if key not in alpha_dict:
        alpha_dict[key] = 1
    else:
        alpha_dict[key] += 1

alpha_dict = sorted(alpha_dict.items(), key=lambda x: x[1], reverse=True)
# print(alpha_dict)

if alpha_dict:
    result = alpha_dict[0][0]
    print(result)
