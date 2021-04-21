# http://codeforces.com/problemset/problem/318/A

n, k = map(int, input().split())

odd_num = [x for x in range(1, n + 1) if x % 2 != 0]
even_num = [x for x in range(1, n + 1) if x % 2 == 0]
# even_num = [x + 1 for x in odd_num]

if k <= (len(odd_num)) and n % 2 == 1:
    print(odd_num[k - 1])

elif k > len(odd_num) and n % 2 == 1:
    print(even_num[k - len(odd_num) - 1])

elif k <= (len(odd_num)) and n % 2 == 0:
    print(odd_num[k - 1])

else:
    print(even_num[k - len(odd_num) - 1])
