# https://codeforces.com/problemset/problem/1676/A

t = int(input())

for _ in range(t):
    ticket = input()
    left_sum = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
    right_sum = int(ticket[3]) + int(ticket[4]) + int(ticket[5])

    if left_sum == right_sum:
        print("YES")
    else:
        print("NO")
