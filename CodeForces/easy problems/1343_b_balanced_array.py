# https://codeforces.com/problemset/problem/1343/B

t = int(input())

for _ in range(t):
    n = int(input())

    odd_array = []
    even_array = []
    if n % 4 == 0:
        print("YES")
        left_side = n // 2
        left_arr = []
        right_arr = []
        left_num = 2
        for x in range(left_side):
            left_arr.append(left_num)
            left_num += 2
        left_sum = sum(left_arr)

        right_num = 1
        for x in range(left_side - 1):
            right_arr.append(right_num)
            right_num += 2
        right_sum = sum(right_arr)
        right_arr.append(left_sum - right_sum)
        print(" ".join(map(str, left_arr)), " ".join(map(str, right_arr)), end=" ")
    else:
        print("NO")
