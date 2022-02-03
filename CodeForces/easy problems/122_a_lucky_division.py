# https://codeforces.com/problemset/problem/122/A

n = int(input())


def lucky_numbers(num):
    num = str(num)
    counter = 0
    for ch in num:
        if ch == "4" or ch == "7":
            counter += 1
    if len(num) == counter:
        return "YES"


k = 0
number = 0
bool_var = True
answer_var = False

if lucky_numbers(n):
    print(lucky_numbers(n))
else:
    while k < n:
        k += 1
        if lucky_numbers(k):
            while number < n:
                number += 1
                if k * number == n:
                    print("YES")
                    bool_var = False
                    answer_var = True
                    break
            number = 0
            if answer_var:
                break
        else:
            continue
    if bool_var:
        print("NO")
