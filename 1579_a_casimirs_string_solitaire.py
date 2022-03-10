# https://codeforces.com/problemset/problem/1579/A

t = int(input())
result = ""

for _ in range(t):
    s = input()
    a = s.count("A")
    b = s.count("B")
    c = s.count("C")

    if "A" in s and "B" in s and "C" in s:
        if a + c == b:
            result = "YES"
        else:
            result = "NO"
    elif "A" in s:
        if a == b:
            result = "YES"
        else:
            result = "NO"
    else:
        if b == c:
            result = "YES"
        else:
            result = "NO"
    print(result)
