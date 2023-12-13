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


def find_row(mirror, smudge=False):
    height = len(mirror)
    for i in range(1, height):
        length = min(i, height-i)
        reflection = True
        for j in range(length):
            if mirror[i-j-1] != mirror[i+j]:
                reflection = False
                break
        if reflection:
            return i
    return False


def find_column(mirror):
    height = len(mirror)
    width = len(mirror[0])
    for i in range(1, width):
        length = min(i, width-i)
        reflection = True
        for j in range(length):
            left = [mirror[x][i-j-1] for x in range(height)]
            right = [mirror[x][i+j] for x in range(height)]
            if left != right:
                reflection = False
                break
        if reflection:
            return i
    return False


def find_row_with_smudge(mirror):
    height = len(mirror)
    for i in range(1, height):
        length = min(i, height-i)
        number_of_smudges_needed = 0
        for j in range(length):
            if mirror[i-j-1] == mirror[i+j]:
                continue
            elif number_of_smudges_needed == 0:
                number_of_unequal_characters = 0
                for left, right in zip(mirror[i-j-1], mirror[i+j]):
                    if left != right:
                        number_of_unequal_characters += 1
                if number_of_unequal_characters == 1:
                    number_of_smudges_needed += 1
                    continue
            break
        if number_of_smudges_needed == 1:
            return i
    return False


def find_column_with_smudge(mirror):
    height = len(mirror)
    width = len(mirror[0])
    for i in range(1, width):
        length = min(i, width-i)
        number_of_smudges_needed = 0
        for j in range(length):
            left = [mirror[x][i-j-1] for x in range(height)]
            right = [mirror[x][i+j] for x in range(height)]
            if left == right:
                continue
            elif number_of_smudges_needed == 0:
                number_of_unequal_characters = 0
                for l, r in zip(left, right):
                    if l != r:
                        number_of_unequal_characters += 1
                if number_of_unequal_characters == 1:
                    number_of_smudges_needed += 1
                    continue
            break
        if number_of_smudges_needed == 1:
            return i
    return False


if __name__ == "__main__":
    mirrors = readfile("input.txt")
    total_sum = 0
    for i, mirror in enumerate(mirrors):
        row = find_row(mirror)
        column = find_column(mirror)
        if isinstance(row, int):
            total_sum += 100*row
        elif isinstance(column, int):
            total_sum += column
    print("Part 1:", total_sum)

    total_sums = []
    for i, mirror in enumerate(mirrors):
        row = find_row_with_smudge(mirror)
        column = find_column_with_smudge(mirror)
        if isinstance(row, int) and isinstance(column, int):
            print(i, "Both row and column is int")
        elif isinstance(row, int):
            total_sum += 100*row
        elif isinstance(column, int):
            total_sum += column
    print("Part 2:", total_sum)

# 34382 too low