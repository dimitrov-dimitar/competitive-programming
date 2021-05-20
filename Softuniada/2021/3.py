all_bonuses = []


while True:
    name = input()
    if name == 'stop':
        break
    tasks = [int(x) for x in input().split(', ')]
    # print(tasks)
    bonuses_per_user = 0
    for num in tasks:
        result = 1
        index = tasks.index(num)
        tasks.pop(index)
        for n in tasks:
            if n == 0:
                result = 0
                break
            result *= n
        bonuses_per_user += result
        tasks.insert(index, num)

    print(f'{name} has a bonus of {bonuses_per_user} lv.')
    all_bonuses.append(bonuses_per_user)

print(f'The amount of all bonuses is {sum(all_bonuses)} lv.')
