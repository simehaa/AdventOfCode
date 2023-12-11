def readfile(filename):
    grid = []
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = [c for c in line.rstrip()]
            grid.append(line)
            if "#" not in line:
                grid.append(line)  
    columns_without_galaxies = []
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
    for y, row in enumerate(grid):
        for i, x in enumerate(columns_without_galaxies):
            grid[y] = grid[y][:x+i+1] + grid[y][x+i:]
    return grid


def solve(grid):
    idx = []

    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if grid[y][x] == "#":
                idx.append((y, x))
    lengths = []
    ctr = 0
    for i in range(len(idx)):
        for j in range(i+1, len(idx)):
            y0, x0 = idx[i]
            y1, x1 = idx[j]
            lengths.append(abs(y1-y0)+abs(x1-x0))

    print(sum(lengths))


if __name__ == "__main__":
    grid = readfile("input.txt")
    solve(grid)

