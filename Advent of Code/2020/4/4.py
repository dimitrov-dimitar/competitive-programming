matrix = []

with open("input") as f:
    for row in f:
        row_matrix = [x for x in row.split()]
        matrix.append(row_matrix)

# print(matrix)

# requirements = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
# counter = 0
# valid_pasport = 0


# for row in matrix:
#     if not row:
#         counter = 0
#         continue
#     for elements in row:
#         for single_requirements in requirements:
#             if single_requirements in elements:
#                 counter += 1
#         if counter == 7:
#             valid_pasport += 1

# print(valid_pasport)

requirements = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
counter = 0
valid_pasport = 0
temp_set = set()
pasport_count = 0


def solve(elements):
    prefix = elements.split(":")[0]
    suffix = elements.split(":")[1]
    if prefix == "byr":
        if 1920 <= int(suffix) <= 2002:
            return True
    elif prefix == "iyr":
        if 2010 <= int(suffix) <= 2020:
            return True
    elif prefix == "eyr":
        if 2020 <= int(suffix) <= 2030:
            return True
    elif prefix == "hgt":
        if "cm" in suffix:
            centimeters = int(suffix.split("c")[0])
            if 150 <= centimeters <= 193:
                return True
        elif "in" in suffix:
            inches = int(suffix.split("i")[0])
            if 59 <= inches <= 76:
                return True
    elif prefix == "hcl":
        if "#" in suffix:
            chars = suffix.split("#")[1]
            ok = "0123456789abcdef"
            if len(chars) == 6 and all(c in ok for c in chars):
                return True
    elif prefix == "ecl":
        ok = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if suffix in ok:
            return True
    elif prefix == "pid":
        if len(suffix) == 9 and suffix.isdigit():
            return True


for row in matrix:
    if not row:
        temp_set = set()
        pasport_count += 1
        continue
    for elements in row:
        if "cid" in elements:
            continue
        for single_requirements in requirements:
            if single_requirements in elements and solve(elements):
                temp_set.add(single_requirements)
        if requirements == temp_set:
            valid_pasport += 1
            # break

print(valid_pasport)
# print(pasport_count)
