# https://codeforces.com/problemset/problem/118/A

text = input()

vowels = ["A", "O", "Y", "E", "U", "I"]
new_text = ''

for char in text:
    if char.upper() in vowels:
        new_text += ''
    else:
        new_text += '.' + char.lower()

print(new_text)
