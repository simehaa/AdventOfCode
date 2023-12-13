def readfile(filename):
    mirrors = []
    with open(filename, "r") as f:
        lines = f.readlines()
        mirror = []
        for line in lines:
            if len(line) <= 1:
                mirrors.append(mirror)
                mirror = []
            else:
                row = line.rstrip()
                mirror.append(row)
    mirrors.append(mirror)
    return mirrors


def find_row(mirror, smudges=0):
    height = len(mirror)
    for i in range(1, height):
        length = min(i, height-i)
        number_of_smudges_needed = 0
        for j in range(length):
            if mirror[i-j-1] != mirror[i+j]:
                for left, right in zip(mirror[i-j-1], mirror[i+j]):
                    if left != right:
                        number_of_smudges_needed += 1
                continue
        if number_of_smudges_needed == smudges:
            return i
    return 0


def find_column(mirror, smudges=0):
    height = len(mirror)
    width = len(mirror[0])
    for i in range(1, width):
        length = min(i, width-i)
        number_of_smudges_needed = 0
        for j in range(length):
            left = [mirror[x][i-j-1] for x in range(height)]
            right = [mirror[x][i+j] for x in range(height)]
            if left != right:
                for l, r in zip(left, right):
                    if l != r:
                        number_of_smudges_needed += 1
                continue
        if number_of_smudges_needed == smudges:
            return i
    return 0


if __name__ == "__main__":
    for part in [1, 2]:
        total_sum = 0
        for mirror in readfile("input.txt"):
            total_sum += 100*find_row(mirror, smudges=part-1)
            total_sum += find_column(mirror, smudges=part-1)
        print(f"Part {part}:", total_sum)
