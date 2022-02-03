# https://codeforces.com/problemset/problem/703/A

n = int(input())

m_counter = 0
c_counter = 0

for _ in range(n):
    x, y = [int(x) for x in input().split()]
    if x == y:
        m_counter += 1
        c_counter += 1
    elif x > y:
        m_counter += 1
    else:
        c_counter += 1

if m_counter > c_counter:
    print("Mishka")
elif m_counter < c_counter:
    print("Chris")
else:
    print("Friendship is magic!^^")
