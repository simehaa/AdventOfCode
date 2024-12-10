def scan_cave(filename, floor=False):
    height, width = 200, 800
    grid = [["."] * width for _ in range(height)]
    grid[0][500] = "+"
    lowest_rock = 0
    with open(filename) as f:
        for line in f:
            coordinates = line.replace("\n", "").split(" -> ")
            for i in range(len(coordinates) - 1):
                y0, x0 = coordinates[i].split(",")
                y1, x1 = coordinates[i + 1].split(",")
                x0 = int(x0)
                y0 = int(y0)
                x1 = int(x1)
                y1 = int(y1)
                lowest_rock = max(lowest_rock, x0, x1)
                if x0 == x1:
                    for y in range(min(y0, y1), max(y0, y1) + 1):
                        grid[x0][y] = "#"
                if y0 == y1:
                    for x in range(min(x0, x1), max(x0, x1) + 1):
                        grid[x][y0] = "#"
    if floor:
        for i in range(width):
            grid[lowest_rock + 2][i] = "#"

    return grid


def move(grid, x, y):
    if x == len(grid) - 1:
        return grid, "abyss"
    if grid[x + 1][y] == ".":
        return move(grid, x + 1, y)
    if grid[x + 1][y - 1] == ".":
        return move(grid, x + 1, y - 1)
    if grid[x + 1][y + 1] == ".":
        return move(grid, x + 1, y + 1)
    if x == 0 and y == 500:
        grid[x][y] = "O"
        return grid, "filled"
    grid[x][y] = "O"
    return grid, "rockslide"


def solve(filename, floor=False):
    grid = scan_cave(filename, floor=floor)
    while True:
        grid, status = move(grid, 0, 500)
        if status == "abyss" or status == "filled":
            break
    sand = 0
    for row in grid:
        sand += row.count("O")

    return sand


if __name__ == "__main__":
    print("Part 1:", solve("test.txt", floor=False))
    print("Part 2:", solve("test.txt", floor=True))
