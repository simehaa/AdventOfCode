def readfile(filename):
    grid = []
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            grid.append(line.rstrip())
    return grid


def solve(grid):
    start_position = [-1, -1]
    height = len(grid)
    width = len(grid[0])
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == "S":
                start_position = [i, j]
                break

    y, x = start_position
    paths = [[[y, x]], [[y, x]]]
    if x-1 >= 0:
        if grid[y][x-1] in ["L", "F", "-"]:
            paths[len(paths[0])-1].append([y, x-1])
    if x+1 < width:
        if grid[y][x+1] in ["J", "7", "-"]:
            paths[len(paths[0])-1].append([y, x+1])
    if y-1 >= 0:
        if grid[y-1][x] in ["F", "7", "|"]:
            paths[len(paths[0])-1].append([y-1, x])
    if y+1 < height:
        if grid[y+1][x] in ["L", "J", "|"]:
            paths[len(paths[0])-1].append([y+1, x])

    while paths[0][-1] != paths[1][-1]:
        for path in paths:
            y, x = path[-1]
            if grid[y][x] == "|":
                if path[-2][0] < y:
                    path.append([y+1, x])
                else:
                    path.append([y-1, x])
            elif grid[y][x] == "-":
                if path[-2][1] < x:
                    path.append([y, x+1])
                else:
                    path.append([y, x-1])
            elif grid[y][x] == "L":
                if path[-2][0] < y:
                    path.append([y, x+1])
                else:
                    path.append([y-1, x])
            elif grid[y][x] == "J":
                if path[-2][0] < y:
                    path.append([y, x-1])
                else:
                    path.append([y-1, x])
            elif grid[y][x] == "7":
                if path[-2][1] < x:
                    path.append([y+1, x])
                else:
                    path.append([y, x-1])
            elif grid[y][x] == "F":
                if path[-2][0] > y:
                    path.append([y, x+1])
                else:
                    path.append([y+1, x])
            elif grid[y][x] == ".":
                raise ValueError("Broke the pipe loop")
            elif grid[y][x] == "S":
                raise ValueError("Returned to start")
            
    unique_path = paths[0]
    for path in paths[1][::-1]:
        if path not in unique_path:
            unique_path.append(path)
        
    return unique_path 


def number_of_elements_enclosed_by_loop(grid, path, print_expanded_grid=False):
    height = len(grid)
    width = len(grid[0])
    # Double up the grid and pad it on low indices (high indices not needed)
    # All odd coordinates are "real"
    # All even coordinates are "ghost"
    # First: we extend the loop by filling "|"" or "-" at ghost coordinates
    # Then: we do an extended searh on the outside of the loop
    #   this area is referred to as "air"
    #   we are allowed to search on ghost coordinates to
    #   get inside the loop using allowed mechanics
    new_grid = [["."]*(2*width+1) for _ in range(2*height+1)]
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            new_grid[2*y+1][2*x+1] = c

    # First, we extend the loop to ghost coordinates
    new_path = []
    for i in range(len(path)):
        y1, x1 = path[i%len(path)]
        y2, x2 = path[(i+1)%len(path)]
        yn = 2*y1+1
        xn = 2*x1+1
        new_path.append((yn, xn))
        if x2 != x1:
            xn += x2 - x1
            new_path.append((yn, xn))
            new_grid[yn][xn] = "-"
        if y2 != y1:
            yn += y2 - y1
            new_path.append((yn, xn))
            new_grid[yn][xn] = "|"
    
    # Second, perform the extended search
    air = [(0, 0)]
    zeros = 0
    ones = 0
    for y, x in air:
        neighbors = [
            (y+1,x), # down
            (y-1,x), # up
            (y,x+1), # right
            (y,x-1), # left
        ]
        for yn, xn in neighbors:
            if xn < 0 or xn >= 2*width + 1 or yn < 0 or yn >= 2*height + 1 or (yn, xn) in air:
                continue
            elif (yn, xn) not in air and (yn, xn) not in new_path:
                air.append((yn, xn))
                if yn % 2 == 1 and xn % 2 == 1:
                    new_grid[yn][xn] = "0"
                    zeros += 1

    # Fill in the possible places for "1" (real coordinates inside the loop)
    for y in range(2*height):
        for x in range(2*width):
            if y % 2==1 and x % 2==1 and new_grid[y][x] != "0" and (y, x) not in new_path:
                new_grid[y][x] = "1"
                ones += 1

    if print_expanded_grid:
        for row in new_grid:
            print("".join(row))
    
    return ones

if __name__ == "__main__":
    grid = readfile("test.txt")
    path = solve(grid)
    print("Part 1 (test):", int(len(path)/2))
    print("Part 2 (test):", number_of_elements_enclosed_by_loop(grid, path, print_expanded_grid=True))

    grid = readfile("input.txt")
    path = solve(grid)
    print("Part 1:", int(len(path)/2))
    print("Part 2:", number_of_elements_enclosed_by_loop(grid, path, print_expanded_grid=False))
