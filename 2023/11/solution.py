def readfile(filename):
    grid = []
    columns_without_galaxies = []
    rows_without_galaxies = []
    with open(filename, "r") as f:
        lines = f.readlines()
        for y, line in enumerate(lines):
            grid.append([c for c in line.rstrip()])
            if "#" not in line:
                rows_without_galaxies.append(y)
    height = len(grid)
    width = len(grid[0])
    for x in range(width):
        galaxies = False
        for y in range(height):
            if grid[y][x] == "#":
                galaxies = True
                break
        if not galaxies:
            columns_without_galaxies.append(x)
    return grid, rows_without_galaxies, columns_without_galaxies


def solve(filename, replace=2):
    grid, rows_without_galaxies, columns_without_galaxies = readfile(filename)
    idx = []
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if grid[y][x] == "#":
                idx.append((y, x))
    lengths = 0
    for i in range(len(idx)):
        for j in range(i+1, len(idx)):
            y0, x0 = idx[i]
            y1, x1 = idx[j]
            distance = abs(y1-y0)+abs(x1-x0)
            for y in rows_without_galaxies:
                if (y > y0 and y < y1) or (y > y1 and y < y0):
                    distance += replace-1
            for x in columns_without_galaxies:
                if (x > x0 and x < x1) or (x > x1 and x < x0):
                    distance += replace-1
            lengths += distance
    return lengths


if __name__ == "__main__":
    print("Part 1 (test):", solve("test.txt"))
    print("Part 1:", solve("input.txt"))
    print("Part 2 (test):",solve("test.txt", replace=100))
    print("Part 2:", solve("input.txt", replace=1_000_000))

