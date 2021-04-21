# http://codeforces.com/problemset/problem/318/A

n, k = map(int, input().split())

odd_num = [x for x in range(1, n + 1) if x % 2 != 0]
even_num = [x for x in range(1, n + 1) if x % 2 == 0]

all_num = odd_num + even_num
print(all_num[k - 1])
