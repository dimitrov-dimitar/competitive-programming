    for char in range(1, len(shuffle_m)):
        correct_ch = correct_m[char]
        shuffle_ch = shuffle_m[char]
        if correct_ch != shuffle_ch:
            shuffle_m.remove(correct_ch)
            shuffle_m.insert(char, correct_ch)
            counter += 1