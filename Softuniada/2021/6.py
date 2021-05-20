shuffle = input()
correct = input()

shuffle_m = []
correct_m = []
counter = 0

for ch in shuffle:
    shuffle_m.append(ch)

for ch in correct:
    correct_m.append(ch)

# if shuffle_m[0].isupper():
#     counter += 1
# else:
#     for ch in shuffle_m:
#         if ch.isupper():
#             shuffle_m.remove(ch)
#             shuffle_m.insert(0, ch)
#             counter += 1


sum_shuffle = 0
sum_correct = 0

for ch in shuffle_m:
    sum_shuffle += ord(ch)
for ch in correct_m:
    sum_correct += ord(ch)

if sum_correct != sum_shuffle:
    print('The name cannot be transformed!')
else:
    for char in range(len(shuffle_m) - 1, 0, -1):

        correct_ch = correct_m[char]
        shuffle_ch = shuffle_m[char]
        if correct_ch != shuffle_ch:
            shuffle_m.remove(correct_ch)
            shuffle_m.insert(0, correct_ch)
            counter += 1
    print(f'The minimum operations required to convert "{shuffle}" to "{correct}" are {counter}')
