# https://codeforces.com/problemset/problem/281/A

text_input = input()

first = text_input[0]

if first.islower():
    first = first.capitalize()

print(first + text_input[1:])
