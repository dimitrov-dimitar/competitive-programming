# https://codeforces.com/problemset/problem/158/B

n = int(input())
s = [int(x) for x in input().split()]

sum_s = sum(s)
taxi = 0

s = sorted(s, reverse=True)

four = s.count(4)
three = s.count(3)
two = s.count(2)
one = s.count(1)

# four
taxi += four

# two
if two == 1:
    taxi += 1
elif two % 2 == 0:
    taxi += two / 2
else:
    taxi += (two / 2) + 1

# three and one
reminder = one - three
if three > one:
    taxi += three
elif three == one:
    taxi += three
elif three < one:
    taxi += three
    if two % 2 == 0:
        if reminder % 4 == 0:
            taxi += (reminder / 4)
        else:
            taxi += (reminder // 4) + 1
    else:
        if reminder > 2:
            reminder -= 2
            if reminder % 4 == 0:
                taxi += (reminder / 4)
            else:
                taxi += (reminder // 4) + 1

print(int(taxi))
