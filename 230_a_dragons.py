# https://codeforces.com/problemset/problem/230/A

from collections import defaultdict

s, n = [int(x) for x in input().split()]

dragons = defaultdict(list)
dragons_new = defaultdict(list)


for _ in range(n):
    x, y = [int(x) for x in input().split()]
    dragons[x].append(y)

dragons = dict(sorted(dragons.items()))
bool_var = True


for k, v in dragons.items():
    v = sorted(v, reverse=True)
    dragons_new[k] = v

# print(dragons)
print(dragons_new)

for dragon in dragons_new:
    if s > dragon:
        s += dragons_new[dragon][0]
        
    else:
        print('NO')
        bool_var = False
        break

if bool_var:
    print('YES')
