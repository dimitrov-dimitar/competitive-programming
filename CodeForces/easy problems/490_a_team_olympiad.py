# https://codeforces.com/problemset/problem/490/A

n = int(input())
childrens = [int(x) for x in input().split()]


count_one = 0
count_two = 0
count_three = 0

if 1 in childrens and 2 in childrens and 3 in childrens:
    count_one = childrens.count(1)
    count_two = childrens.count(2)
    count_three = childrens.count(3)
    w = min(count_one, count_two, count_three)
    print(w)
    ones = [i + 1 for i, num in enumerate(childrens) if num == 1]
    twos = [i + 1 for i, num in enumerate(childrens) if num == 2]
    threes = [i + 1 for i, num in enumerate(childrens) if num == 3]
    # print(ones)
    # print(twos)
    # print(threes)
    for i in range(w):
        print(ones[i], twos[i], threes[i])
else:
    print(0)
