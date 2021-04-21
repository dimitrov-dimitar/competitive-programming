# https://codeforces.com/problemset/problem/227/B


def main():
    n = int(input())
    n_list = [int(x) for x in input().split()]
    m = int(input())
    m_list = [int(x) for x in input().split()]

    counter_l_r = 0
    counter_r_l = 0

    for q in m_list:
        counter_l_r = counter_l_r + n_list.index(q) + 1
        counter_r_l = counter_r_l + len(n_list) - n_list.index(q)

    print(counter_l_r, counter_r_l)


main()
