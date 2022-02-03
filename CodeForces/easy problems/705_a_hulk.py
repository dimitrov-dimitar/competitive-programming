# https://codeforces.com/problemset/problem/705/A

n = int(input())

love = "I love it"
hate = "I hate it"
result = ""

if n == 1:
    print("I hate it")
else:
    for num in range(1, n + 1):
        if num == n:
            if num % 2 != 0:
                result += hate
            else:
                result += love
            break
        if num % 2 != 0:
            result += "I hate that" + " "
        else:
            result += "I love that" + " "

print(result)
