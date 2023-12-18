with open("test.txt") as f:
    lines = f.readlines()
    score = 0
    scratch_cards = [1]*len(lines)
    for i, line in enumerate(lines):
        winning_numbers, my_numbers = line[9:].split("|")
        winning_numbers = [int(n) for n in winning_numbers.split()]
        my_numbers = [int(n) for n in my_numbers.split()]
        matches = len([num for num in my_numbers if num in winning_numbers])
        score += 2**(matches-1) if matches else 0
        for j in range(i+1, i+1+matches):
            scratch_cards[j] += scratch_cards[i]
print(f"Part 1: {score}\nPart 2: {sum(scratch_cards)}")
