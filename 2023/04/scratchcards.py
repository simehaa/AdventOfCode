score = 0
scratch_cards = list(open("test.txt"))
more_scratch_cards = [1] * len(scratch_cards)
for i, line in enumerate(scratch_cards):
    winning_numbers, my_numbers = line[9:].split("|")
    winning_numbers = [int(n) for n in winning_numbers.split()]
    my_numbers = [int(n) for n in my_numbers.split()]
    matches = len([num for num in my_numbers if num in winning_numbers])
    score += 2 ** (matches - 1) if matches else 0
    for j in range(i + 1, i + 1 + matches):
        more_scratch_cards[j] += more_scratch_cards[i]

print("Part 1:", score)
print("Part 2:", sum(more_scratch_cards))
