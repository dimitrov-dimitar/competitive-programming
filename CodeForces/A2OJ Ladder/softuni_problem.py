total_budget = 0

while True:
    destination = input()
    if destination == "End":
        break
    minimal_budget = float(input())
    while True:
        command = input()
        if command == "End":
            break
        money = float(command)
        total_budget += money
        if total_budget >= minimal_budget:
            print(f"Going to {destination}!")
            total_budget = 0
            break
