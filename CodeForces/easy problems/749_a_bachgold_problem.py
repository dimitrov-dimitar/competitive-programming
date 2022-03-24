# https://codeforces.com/problemset/problem/749/A

n = int(input())

if n % 2 == 0:
    result = n // 2
    print(result)
    print("2 " * result)

else:
    multiplier = int((n - 3) / 2)
    print(multiplier + 1)
    print("2 " * multiplier + "3")
