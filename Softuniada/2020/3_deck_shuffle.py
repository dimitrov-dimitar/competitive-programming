n = int(input())
numbers_index = input().split()

deck = []
left_deck = []
right_deck = []


for i in range(1, n + 1):
    deck.append(i)

numbers_index = [int(x) for x in numbers_index]

for index in numbers_index:
    left_deck = deck[:index]
    right_deck = deck[index:]
    deck.clear()

    while len(left_deck) > 0 or len(right_deck) > 0:
        if len(left_deck) == 0:
            pass
        else:
            deck.append(left_deck[0])
            left_deck.pop(0)
        if len(right_deck) == 0:
            pass
        else:
            deck.append(right_deck[0])
            right_deck.pop(0)

deck = [str(x) for x in deck]
print(" ".join(deck))
