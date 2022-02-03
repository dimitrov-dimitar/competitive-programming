# https://codeforces.com/problemset/problem/443/A

set_input = input()

set_input = set_input.replace("{", "")
set_input = set_input.replace("}", "")
set_input = set_input.replace(",", "")
set_input = set_input.replace(" ", "")


result = "".join(set(set_input))

if set_input == "":
    print(0)
else:
    print(len(result))
