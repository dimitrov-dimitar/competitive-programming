# https://codeforces.com/problemset/problem/1669/B

n = int(input())

for _ in range(n):
    t = int(input())
    n_arr = [int(x) for x in input().split()]

    quit_var = False
    num_dict = {}
    for key in n_arr:
        if key not in num_dict:
            num_dict[key] = 1
        else:
            num_dict[key] += 1
            if num_dict[key] >= 3:
                print(key)
                quit_var = True
                break
    if not quit_var:
        print(-1)
