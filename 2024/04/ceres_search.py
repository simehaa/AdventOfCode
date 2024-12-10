def solve(filename):
    with open(filename) as f:
        grid = [l.strip() for l in f.readlines()]
    h = len(grid)
    w = len(grid[0])

    import re

    p = r"(?=(XMAS|SAMX))"
    matches = 0

    # horizontal
    for l in grid:
        matches += len(re.findall(p, l))

    # vertical
    for x in range(w):
        l = "".join([grid[y][x] for y in range(h)])
        matches += len(re.findall(p, l))

    # diagonals
    for d in range(h + w - 1):
        l1 = ""
        l2 = ""
        for x in range(max(0, d - w + 1), min(d + 1, h)):
            y1 = d - x
            y2 = h - 1 - (d - x)
            l1 += grid[y1][x]
            l2 += grid[y2][x]
        matches += len(re.findall(p, l1))
        matches += len(re.findall(p, l2))
    print(matches)


def part2(filename):
    with open(filename) as f:
        grid = [l.strip() for l in f.readlines()]
    h = len(grid)
    w = len(grid[0])
    matches = 0
    for y in range(1, h - 1):
        for x in range(1, w - 1):
            if grid[y][x] != "A":
                continue
            diag = grid[y - 1][x - 1] + grid[y + 1][x + 1]
            if diag not in ["MS", "SM"]:
                continue
            diag = grid[y - 1][x + 1] + grid[y + 1][x - 1]
            if diag not in ["MS", "SM"]:
                continue
            matches += 1
    print(matches)


solve("test.txt")
solve("input.txt")
part2("test.txt")
part2("input.txt")
