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
            
    unique_path = []
    for path in paths[0] + paths[1]:
        if path not in unique_path:
            unique_path.append(path)
        
    return max(len(paths[0]), len(paths[1])) - 1, unique_path


def color_character(self, char):
        cycle = 6*128
        if self.color_counter % cycle < 128:
            self.red += 1
        elif self.color_counter % cycle < 2*128:
            self.red -= 1
        elif self.color_counter % cycle < 3*128:
            self.green += 1
        elif self.color_counter % cycle < 4*128:
            self.green -= 1
        elif self.color_counter % cycle < 5*128:
            self.blue += 1
        elif self.color_counter % cycle < 6*128:
            self.blue -= 1
        self.color_counter += 1
        return f"\033[38;2;{128+self.red};{128+self.green};{128+self.blue}m{char}\033[0m"


def print_loop(grid, path, outside):
    new_grid = []
    for row in grid:
        new_grid.append([c for c in row])
    counter = 0
    length = 128
    cycle = 6*128
    red = 128
    green = 128
    blue = 128
    for y, x in path:
        if counter % cycle < length:
            red += 1
        elif counter % cycle < 2*length:
            red -= 1
        elif counter % cycle < 3*length:
            green += 1
        elif counter % cycle < 4*length:
            green -= 1
        elif counter % cycle < 5*length:
            blue += 1
        elif counter % cycle < 6*length:
            blue -= 1
        counter += 1
        new_grid[y][x] = f"\033[38;2;{red};{green};{blue}m{grid[y][x]}\033[0m"
    for y, x in outside:
        new_grid[y][x] = f"\033[38;2;256;256;256m0\033[0m"
    for row in grid:
        for elem in row:
            print(elem, end="")    


def number_of_elements_enclosed_by_loop(grid, path):
    # Start by padding the grid
    height = len(grid)
    width = len(grid[0])
    pad_width = width + 2
    pad_height = height + 2
    new_grid = [["."]*pad_width]
    for row in grid:
        new_grid.append(["."] + [c for c in row] + ["."])
    new_grid.append(["."]*pad_width)
    new_path = []
    for y, x in path:
        new_path.append((y+1, x+1))

    air = [(0, 0)]
    new_grid[0][0] = "0"
    loop_touching_coordinates = []
    for y, x in air:
        neighbors = [
            (y+1,x), # down
            (y-1,x), # up
            (y,x+1), # right
            (y,x-1), # left
        ]
        for yn, xn in neighbors:
            if xn < 0 or xn >= pad_width or yn < 0 or yn >= pad_height or (yn, xn) in air:
                continue
            elif (yn, xn) not in air and (yn, xn) not in new_path:
                air.append((yn, xn))
                new_grid[yn][xn] = "0"
            if (yn, xn) in new_path and (y, x) not in loop_touching_coordinates:
                loop_touching_coordinates.append((y, x))
    
    for y, x in loop_touching_coordinates:
        new_grid[y][x] = "#"

    for y in range(pad_height):
        for x in range(pad_width):
            if (y, x) not in new_path and (y, x) not in air:
                new_grid[y][x] = "I"

    for row in new_grid:
        print("".join(row))
    
    return pad_width*pad_height - len(path) - len(air)

if __name__ == "__main__":
    grid = readfile("test.txt")
    max_length, path = solve(grid)
    print("Part 1:", max_length)
    print("Part 2:", number_of_elements_enclosed_by_loop(grid, path))
