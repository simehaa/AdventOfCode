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


def find_column(mirror, smudge=False):
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


if __name__ == "__main__":
    mirrors = readfile("input.txt")
    total_sum = 0
    for mirror in mirrors:
        row = find_row(mirror)
        if isinstance(row, int):
            total_sum += 100*row
        column = find_column(mirror)
        if isinstance(column, int):
            total_sum += column
    print(total_sum)
