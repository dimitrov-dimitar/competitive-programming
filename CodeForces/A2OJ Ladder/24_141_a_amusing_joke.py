# https://codeforces.com/problemset/problem/141/A

guest_name = input()
residence_host = input()
pile = list(input())

pile_copy = pile.copy()
combine_name = (guest_name + residence_host)
combine_list = list(combine_name)

for char in combine_list:
    if char in pile:
        pile.remove(char)

counter = len(guest_name) + len(residence_host)
if not pile and counter == len(pile_copy):
    print("YES")
else:
    print("NO")
