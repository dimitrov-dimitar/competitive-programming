# https://codeforces.com/problemset/problem/1342/A

t = int(input())

for _ in range(t):
    num_arr = []
    x, y = [int(x) for x in input().split()]
    a, b = [int(x) for x in input().split()]

    max_num = max(x, y)
    a_multiplier = abs(x - y)
    b_multiplier = max_num - a_multiplier
    mix_a_b = a_multiplier * a + b_multiplier * b
    num_arr.append(mix_a_b)

    a_answer = (x + y) * a
    num_arr.append(a_answer)

    print(min(num_arr))
