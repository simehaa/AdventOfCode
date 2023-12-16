def get_grid(filename, pad=5): 
    unpadded_grid = []
    with open(filename, "r") as f:
        for line in f:
            unpadded_grid.append([i for i in line.rstrip()])

    height, width = len(unpadded_grid), len(unpadded_grid[0])
    grid = []

    for i in range(pad):
        grid.append(["."]*(width + 2*pad))

    for i in range(height):
        grid.append(["."]*pad + unpadded_grid[i] + ["."]*pad)

    for i in range(pad):
        grid.append(["."]*(width + 2*pad))

    return grid


def print_grid(grid):
    for x, l in enumerate(grid):
        for y, c in enumerate(l):
            print(c, end="")
        print()
    print()


if __name__ == "__main__":
    grid = get_grid("test.txt", pad=100)

    NW = (-1,-1)
    N = (-1,0)
    NE = (-1,1)
    W = (0,-1)
    E = (0,1)
    SW = (1,-1)
    S = (1,0)
    SE = (1,1)
    all_directions = (NW, N, NE, W, E, SW, S, SE)

    
    moves = ((NW,N,NE), (SW,S,SE), (NW,W,SW), (NE,E,SE))
    for i in range(1000):
        elves = []
        for x,l in enumerate(grid):
            for y,c in enumerate(l):
                if c == "#":
                    elves.append((x,y))


        ordered_moves = (moves[i%4], moves[(i+1)%4], moves[(i+2)%4], moves[(i+3)%4])
        proposed_coordinates = {}

        # Loop through elves
        for elf_x, elf_y in elves:
            
            for dx, dy in all_directions:
                if grid[elf_x+dx][elf_y+dy] == "#":
                    break
            else:
                continue

            for cornel, direct, corner in ordered_moves:
                if (
                    grid[elf_x+cornel[0]][elf_y+cornel[1]] == "." and
                    grid[elf_x+direct[0]][elf_y+direct[1]] == "." and
                    grid[elf_x+corner[0]][elf_y+corner[1]] == "."
                ):
                    if (elf_x+direct[0], elf_y+direct[1]) not in proposed_coordinates:
                        proposed_coordinates[(elf_x+direct[0], elf_y+direct[1])] = [(elf_x, elf_y)]
                    else:
                        proposed_coordinates[(elf_x+direct[0], elf_y+direct[1])].append((elf_x, elf_y))
                    break
        
        old_grid = grid.copy()
        performed_moves = 0

        for new_coor, elves in proposed_coordinates.copy().items():
            if len(elves) == 1:
                new_x, new_y = new_coor
                grid[new_x][new_y] = "#"
                elf_x, elf_y = elves[0]
                grid[elf_x][elf_y] = "."
                performed_moves += 1

        min_x, max_x, min_y, max_y = len(grid), 0, len(grid[0]), 0
        for x,l in enumerate(grid):
            if "#" in l:
                min_x = min(min_x, x)
                max_x = max(max_x, x)
            for y,c in enumerate(l):
                if c == "#":
                    min_y = min(min_y, y)
                    max_y = max(max_y, y)

        counter = 0
        for x in range(min_x, max_x+1):
            for y in range(min_y, max_y+1):
                if grid[x][y] == ".":
                    counter += 1

        if i == 10 - 1:
            print(f"Part 1: {counter}")

        if performed_moves == 0:
            print(f"Part 2: {i+1}")
            break