def scan_cave(floor=False):
    height, width = 200, 800
    grid = [["."] * width for _ in range(height)]
    grid[0][500] = "+"

    lowest_rock = 0
    with open("input.txt") as f:
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
            grid[lowest_rock+2][i] = "#"

    return grid


def move(grid, x, y):
        if x == len(grid) - 1:
            return grid, "abyss"
        elif grid[x+1][y] == ".":
            return move(grid, x+1, y)
        elif grid[x+1][y-1] == ".":
            return move(grid, x+1, y-1)
        elif grid[x+1][y+1] == ".":
            return move(grid, x+1, y+1)
        elif x == 0 and y == 500:
            grid[x][y] = "O"
            return grid, "filled"
        else:
            grid[x][y] = "O"
            return grid, "rockslide"


def fill(floor=False):
    grid = scan_cave(floor=floor)
    while True:
        grid, status = move(grid, 0, 500)
        if status == "abyss" or status == "filled":
            break

    sand = 0
    for row in grid:
        sand += row.count("O")

    return grid, sand


if __name__ == "__main__":
    grid, sand = fill(floor=False)
    print(f"Rock falling into the abyss: {sand}")

    grid, sand = fill(floor=True)
    print(f"Cave floor: {sand}")
