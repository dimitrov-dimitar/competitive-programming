# https://codeforces.com/problemset/problem/520/A

import string

n = int(input())
text = input()

alphabet = set(string.ascii_lowercase)

if set(text.lower()) >= alphabet:
    print('YES')
else:
    print('NO')
