borze_code = input()
ternary_number = []

i = 0
while i < len(borze_code):
    if borze_code[i] == ".":
        ternary_number.append("0")
        i += 1
    elif borze_code[i] == "-":
        if borze_code[i+1] == ".":
            ternary_number.append("1")
            i += 2
        elif borze_code[i+1] == "-":
            ternary_number.append("2")
            i += 2

print("".join(ternary_number))
