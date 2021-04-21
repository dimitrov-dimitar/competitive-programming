import itertools

n = int(input())
digits = [x for x in input().split()]

# input
"""
4
5 0 5 0
"""

list_digits = []

for l in range(0, len(digits) + 1):
    for subset in itertools.permutations(digits, l):
        list_digits.append("".join(map(str, subset)))


new_list = []
for s in list_digits:
    a = s.lstrip("0")
    new_list.append(a)


new_list = [int(x) for x in new_list]
print(new_list)
