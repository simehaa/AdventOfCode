def solve(sequence, part=1):
    idx = -1 if part == 1 else 0
    sums = 0
    for seq in sequence:
        sequences = [[int(num) for num in seq.split()]]
        while set(sequences[-1]) != {0}:
            sequences.append(
                [sequences[-1][i + 1] - sequences[-1][i] for i in range(len(sequences[-1]) - 1)]
            )
        for i in range(len(sequences) - 1):
            first = sequences[-i - 2][0] - sequences[-i - 1][0]
            last = sequences[-i - 1][-1] + sequences[-i - 2][-1]
            sequences[-i - 2] = [first] + sequences[-i - 2] + [last]
        sums += sequences[0][idx]
    return sums


sequence = list(open("test.txt"))
print("Part 1:", solve(sequence, part=1))
print("Part 2:", solve(sequence, part=2))
