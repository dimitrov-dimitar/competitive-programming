# http://codeforces.com/problemset/problem/59/A

text = input()

upper_counter = 0
lower_counter = 0

for char in text:
    if char.isupper():
        upper_counter += 1
    elif char.islower():
        lower_counter += 1

if lower_counter > upper_counter:
    text = text.lower()
elif upper_counter > lower_counter:
    text = text.upper()
else:
    text = text.lower()

print(text)
