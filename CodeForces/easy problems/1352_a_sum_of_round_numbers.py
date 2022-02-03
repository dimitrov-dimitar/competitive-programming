# https://codeforces.com/problemset/problem/1352/A

t = int(input())

num_list = []

for _ in range(t):
    number = int(input())
    if number in range(10):
        print(1)
        print(number)
    else:
        num_len = len(str(number))
        for ch in str(number):
            num_len -= 1
            if ch != "0":
                num_list.append(int(ch) * 10 ** num_len)
        print(len(num_list))
        for num in num_list:
            print(num, end=" ")
    num_list = []
