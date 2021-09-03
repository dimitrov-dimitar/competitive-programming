# https://codeforces.com/problemset/problem/732/A

k, r = [int(x) for x in input().split()]

counter = 1
exit_var = False

while True:
    if exit_var:
        break
    result = counter * k

    if result % 10 == 0:
        print(counter)
        exit_var = True
    elif (result - r) % 10 == 0:
        print(counter)
        exit_var = True

    counter += 1
