def solve(grid, start=(0, 0, 0, 1)):
    covered = []
    beams = [start] # y, x, vy, vx
    for beam in beams:
        y, x, vy, vx = beam
        covered.append((y, x))
        new_beams = []

        # Let beam continue to pass through grid
        while (
            (grid[y][x] == ".")
            or (grid[y][x] == "-" and vx)
            or (grid[y][x] == "|" and vy)
        ):
            if y+vy < 0 or y+vy >= len(grid) or x+vx < 0 or x+vx >= len(grid[0]):
                break
            y += vy
            x += vx
            covered.append((y, x))

        # Split beam into two new beams
        if (grid[y][x] == "|" and vx) or (grid[y][x] == "-" and vy):
            new_beams.append((y+vx, x+vy, vx, vy))
            new_beams.append((y-vx, x-vy, -vx, -vy))

        # Reflect beam in new direction
        elif grid[y][x] == "/":
            new_beams.append((y-vx, x-vy, -vx, -vy))
        elif grid[y][x] == "\\":
            new_beams.append((y+vx, x+vy, vx, vy))

        # Continue to simulate beams
        for beam in new_beams:
            if (
                beam not in beams # avoid looping beams
                and beam[0] >= 0 and beam[1] >= 0 # only beams within grid
                and beam[0] < len(grid) and beam[1] < len(grid[0])
            ):
                beams.append(beam)

    return len(set(covered))
        

def all_entry_points(grid):
    energized = []
    height = len(grid)
    width = len(grid[0])
    for y in range(height):
        energized.append(solve(grid, start=(y, 0, 0, 1)))
        energized.append(solve(grid, start=(y, width-1, 0, -1)))
    for x in range(width):
        energized.append(solve(grid, start=(0, x, 1, 0)))
        energized.append(solve(grid, start=(height-1, x, -1, 0)))
    return max(energized)


grid = [line.rstrip() for line in open("test.txt")]
print("Part 1:", solve(grid))
print("Part 2:", all_entry_points(grid))
