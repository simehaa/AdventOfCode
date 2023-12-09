def readfile(filename):
    numbers = []
    with open(filename, "r") as f:
        lines = f.readlines()
    return lines


def solve(lines, part=1):
    idx = -1 if part == 1 else 0
    sums = 0
    for line in lines:
        sequences = [[int(num) for num in line.split()]]
        while set(sequences[-1]) != {0}:
            sequences.append([sequences[-1][i+1]-sequences[-1][i] for i in range(len(sequences[-1])-1)])
        for i in range(len(sequences)-1):
            first = sequences[-i-2][0] - sequences[-i-1][0]
            last = sequences[-i-1][-1] + sequences[-i-2][-1]
            sequences[-i-2] = [first] + sequences[-i-2] + [last]
        sums += sequences[0][idx]
    return sums


if __name__ == "__main__":
    print("Part 1 (test):", solve(readfile("test.txt"), part=1))
    print("Part 2 (test):", solve(readfile("test.txt"), part=2))
    print("Part 1:", solve(readfile("input.txt"), part=1))
    print("Part 2:", solve(readfile("input.txt"), part=2))
