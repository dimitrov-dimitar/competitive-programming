# https://codeforces.com/problemset/problem/1472/B

t = int(input())

# to be refactoried

for _ in range(t):
    list_1 = []
    list_2 = []
    yes_var = ""
    break_var = False

    n = int(input())
    num_arr = [int(x) for x in input().split()]
    for num in num_arr:
        if num == 1:
            list_1.append(num)
        else:
            list_2.append(num)

    sum_list = sum(list_1) + sum(list_2)

    if sum_list % 2 == 1:
        print("NO")
    else:
        target = sum_list / 2

        for _ in range(len(list_1) + len(list_2)):
            if break_var:
                break
            for a in range(len(list_1) + 1):
                if break_var:
                    break
                for b in range(len(list_2) + 1):
                    if a + 2 * b == target:
                        yes_var = True
                        break_var = True
                        break
        if yes_var:
            print("YES")
        else:
            print("NO")
