def solve(grid, start=(0, 0, 0, 1)):
    covered = []
    beams = [start] # y, x, vy, vx
    for beam in beams:
        y, x, vy, vx = beam
        if (y, x) not in covered:
            covered.append((y, x))
        new_beams = []
        # beam passes through "." or along splitter
        if (
            (grid[y][x] == ".")
            or (grid[y][x] == "-" and vx)
            or (grid[y][x] == "|" and vy)
        ):
            new_beams.append((y+vy, x+vx, vy, vx))

        # splitter 
        elif (grid[y][x] == "|" and vx) or (grid[y][x] == "-" and vy):
            new_beams.append((y+vx, x+vy, vx, vy))
            new_beams.append((y-vx, x-vy, -vx, -vy))

        elif grid[y][x] == "/":
            new_beams.append((y-vx, x-vy, -vx, -vy))

        elif grid[y][x] == "\\":
            new_beams.append((y+vx, x+vy, vx, vy))

        for beam in new_beams:
            if (
                beam not in beams 
                and beam[0] >= 0 and beam[1] >= 0
                and beam[0] < len(grid) and beam[1] < len(grid[0])
            ):
                beams.append(beam)

    return len(covered)
        

def all_entry_points(grid):
    energized = []
    height = len(grid)
    width = len(grid[0])
    simulations = 2*height + 2*width
    for y in range(height):
        print(f"\r{y+1}/{simulations}", end="")
        energized.append(solve(grid, start=(y, 0, 0, 1)))
    for y in range(height):
        print(f"\r{y+1+height}/{simulations}", end="")
        energized.append(solve(grid, start=(y, width-1, 0, -1)))
    for x in range(width):
        print(f"\r{x+1+2*height}/{simulations}", end="")
        energized.append(solve(grid, start=(0, x, 1, 0)))
    for x in range(width):
        print(f"\r{x+1+width+2*height}/{simulations}", end="")
        energized.append(solve(grid, start=(height-1, x, -1, 0)))
    print()
    return max(energized)


if __name__ == "__main__":
    with open("test.txt" ,"r") as f:
        grid = [line.rstrip() for line in f]

    print("Part 1:", solve(grid))
    print("Part 2:", all_entry_points(grid))
