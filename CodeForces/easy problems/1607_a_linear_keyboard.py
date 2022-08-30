# https://codeforces.com/problemset/problem/1607/A

t = int(input())

for _ in range(t):
    keyboard = input()
    s = input()

    keyboard_dict = {}
    for count, letter in enumerate(keyboard):
        keyboard_dict[letter] = count

    units = 0
    for i in range(len(s) - 1):
        current = s[i]
        next = s[i + 1]
        units += abs(keyboard_dict[current] - keyboard_dict[next])
    print(units)
