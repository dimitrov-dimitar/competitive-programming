num_1 = input()
num_2 = input()
num_3 = input()

is_bool = True

perm_1 = int(num_1 + num_2 + num_3)
perm_2 = int(num_1 + num_3 + num_2)
perm_3 = int(num_2 + num_1 + num_3)
perm_4 = int(num_2 + num_3 + num_1)
perm_5 = int(num_3 + num_1 + num_2)
perm_6 = int(num_3 + num_2 + num_1)
sum_num = int(num_1) + int(num_2) + int(num_3)

list_num = [perm_1, perm_2, perm_3, perm_4, perm_5, perm_6]

if num_1 == "0" and num_2 == "0" and num_3 == "0":
    print("No digitivision possible.")
else:
    for i in list_num:
        if i % sum_num == 0:
            print("Digitivision successful!")
            is_bool = False
            break

    if is_bool:
        print("No digitivision possible.")
