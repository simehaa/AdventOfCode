def readfile(filename):
    rocks = []
    squares = []
    grid = []
    with open(filename, "r") as f:
        lines = f.readlines()
        height = len(lines)
        width = len(lines[0])
        for y, line in enumerate(lines):
            line = line.rstrip()
            row = []
            for x, char in enumerate(line):
                row.append(char)
                if char == "O":
                    rocks.append((y, x))
                elif char == "#":
                    squares.append((y, x))
            grid.append(row)
    return rocks, squares, height, width, grid


def print_disc(grid):
    for row in grid:
        print("".join(row))


if __name__ == "__main__":
    rocks, squares, height, width, grid = readfile("test.txt")
    print_disc(grid)
    
    moves = True
    while moves:
        moves = False
        for y, row in enumerate(grid):
            for x, char in enumerate(row):
                if char == "O" and y >= 1 and grid[y-1][x] == ".":
                    grid[y-1][x] = "O"
                    grid[y][x] = "."
                    moves = True
        # print()
        # print_disc(grid)

    load = 0
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == "O":
                load += height-y
    print(load)



# 34382 too low
# 34419 not right
# 66819 too high