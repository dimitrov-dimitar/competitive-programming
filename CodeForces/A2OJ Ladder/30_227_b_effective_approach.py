# https://codeforces.com/problemset/problem/227/B

n = int(input())
n_list = [int(x) for x in input().split()]
m = int(input())
m_list = [int(x) for x in input().split()]

counter_l_r = 0
counter_r_l = 0

for q in m_list:
    for i in n_list:
        counter_l_r += 1
        if q == i:
            break

n_list.reverse()

for q in m_list:
    for i in n_list:
        counter_r_l += 1
        if q == i:
            break

print(counter_l_r, counter_r_l)
