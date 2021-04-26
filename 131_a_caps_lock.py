# https://codeforces.com/problemset/problem/131/A

text = input()


def firs_rule(string):
    # count_upper = 0
    # for ch in string:
    #     if ch.isupper():
    #         count_upper += 1
    # if count_upper == len(string):
    #     return True
    if all(l.isupper() for l in string):
        return True


def second_rule(string):
    if len(string) == 1 and string[0].islower():
        return True
    if string[0].islower() and all(l.isupper() for l in string[1:]):
        return True


new_string = ''
if firs_rule(text) or second_rule(text):
    for ch in text:
        if ch.isupper():
            new_string += ch.lower()
        else:
            new_string += ch.upper()
    print(new_string)
else:
    print(text)
