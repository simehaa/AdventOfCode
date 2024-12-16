def read(filename):
    with open(filename) as f:
        grid, moves = f.read().split("\n\n")
    grid = [list(r) for r in grid.splitlines()]
    moves = moves.replace("\n", "")
    translate = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}
    return grid, [translate[m] for m in moves]


def initial_position(grid):
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == "@":
                return y, x
    return None


def GPS(grid, box_char):
    total = 0
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == box_char:
                total += 100 * y + x
    return total


def part1(grid, moves):
    robot = initial_position(grid)
    for dy, dx in moves:
        y, x = robot
        while True:
            ny, nx = y + dy, x + dx
            if grid[ny][nx] == ".":
                ry, rx = robot
                grid[ry][rx] = "."
                ry, rx = ry + dy, rx + dx
                grid[ny][nx] = "O"
                grid[ry][rx] = "@"
                robot = ry, rx
                break
            if grid[ny][nx] == "O":
                y, x = ny, nx
                continue
            break
    return GPS(grid, "O")


def part2(grid, moves):
    for i, row in enumerate(grid):
        new_row = []
        for c in row:
            if c == "O":
                new_row += ["[", "]"]
            elif c == "@":
                new_row += ["@", "."]
            else:
                new_row += [c, c]
        grid[i] = new_row
    robot = initial_position(grid)
    for i, (dy, dx) in enumerate(moves):
        y, x = robot
        ny, nx = y + dy, x + dx
        # Immediate stop
        if grid[ny][nx] == "#":
            continue
        # Immediate move
        if grid[ny][nx] == ".":
            robot = ny, nx
            grid[y][x] = "."
            grid[ny][nx] = "@"
            continue
        # Ahead IS a box
        if grid[ny][nx] == "]":
            nx -= 1  # Only store the "[" coordinates
        # For all coordinates in boxes_to_move
        # if any wall, break
        # if any boxes, add to boxes_to_move
        boxes_to_move = [(ny, nx)]
        for y, x in boxes_to_move:
            # Horizontal movement: only need to check one location
            if dy == 0:
                ny = y
                nx = x + dx
                if dx == 1:  # right: jump two locations
                    nx = x + 2 * dx
                if grid[ny][nx] == "#":
                    break
                if grid[ny][nx] == "[":
                    boxes_to_move.append((ny, nx))
                if grid[ny][nx] == "]":
                    boxes_to_move.append((ny, nx - 1))
            # Vertical movement: need to check two locations
            else:
                ny, nx = y + dy, x + dx
                left = grid[ny][nx]
                right = grid[ny][nx + 1]
                if left == "#" or right == "#":
                    break
                if left == "[":  # implies right == "]"
                    boxes_to_move.append((ny, nx))
                if right == "[":
                    boxes_to_move.append((ny, nx + 1))
                if left == "]":
                    boxes_to_move.append((ny, nx - 1))
        else:
            # Moving phase
            for y, x in boxes_to_move:
                grid[y][x] = "."
                grid[y][x + 1] = "."
            for y, x in boxes_to_move:
                ny, nx = y + dy, x + dx
                grid[ny][nx] = "["
                grid[ny][nx + 1] = "]"
            ry, rx = robot
            grid[ry][rx] = "."
            ry, rx = ry + dy, rx + dx
            grid[ry][rx] = "@"
            robot = ry, rx
    return GPS(grid, "[")


if __name__ == "__main__":
    print(part1(*read("test.txt")))
    print(part2(*read("test.txt")))
    print(part1(*read("input.txt")))
    print(part2(*read("input.txt")))
