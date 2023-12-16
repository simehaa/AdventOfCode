def read_input(filename="test.txt"):
    with open(filename, "r") as f:
        jets = []
        arrows = [c for c in f.readline()]
        for arrow in arrows:
            if arrow == "<":
                jets.append(-1)
            elif arrow == ">":
                jets.append(1)
    return jets


def print_grid(grid):
    n = len(grid)
    for i, row in enumerate(grid[::-1]):
        print(f"{n-i:4d}|{''.join(row)}|")
    print(f"{0:4d}+-------+")


def print_two_parts(grid, range1, range2):
    for r1, r2 in zip(range1[::-1], range2[::-1]):
        print(f"{r1:4d}|{''.join(grid[r1])}|{''.join(grid[r2])}|{r2}")
    print(f"    +-------+-------+")


def let_rocks_fall(filename, n_rocks=2022):
    jets = read_input(filename)
    jet = 0
    grid = []
    heights = {}
    uniques = {}

    for current_rock in range(n_rocks):
        rock_type = current_rock % 5
        grid.append(["."]*7)
        grid.append(["."]*7)
        grid.append(["."]*7)
        if rock_type == 0:
            grid.append([".", ".", "@", "@", "@", "@", "."])
        elif rock_type == 1:
            grid.append([".", ".", ".", "@", ".", ".", "."])
            grid.append([".", ".", "@", "&", "@", ".", "."])
            grid.append([".", ".", ".", "&", ".", ".", "."])
        elif rock_type == 2:
            grid.append([".", ".", "@", "@", "@", ".", "."])
            grid.append([".", ".", ".", ".", "&", ".", "."])
            grid.append([".", ".", ".", ".", "&", ".", "."])
        elif rock_type == 3:
            grid.append([".", ".", "@", ".", ".", ".", "."])
            grid.append([".", ".", "&", ".", ".", ".", "."])
            grid.append([".", ".", "&", ".", ".", ".", "."])
            grid.append([".", ".", "&", ".", ".", ".", "."])
        elif rock_type == 4:
            grid.append([".", ".", "@", "@", ".", ".", "."])
            grid.append([".", ".", "&", "&", ".", ".", "."])

        for j in range(len(grid)):
            # Reset temporary variables, and determine jet direction
            indices = []
            rows = []
            jet %= len(jets)
            side = jets[jet]
            jet += 1
            can_move_down = True
            can_move_sideways = True
            leftmost = {}
            rightmost = {}

            # Record the indices of the falling rock
            for row in range(len(grid)):
                for col in range(7):
                    rock = grid[row][col]
                    if rock in ["@", "&"]:
                        indices.append([row, col, rock])
                        if row not in leftmost:
                            leftmost[row] = col
                        else:
                            leftmost[row] = min(col, leftmost[row])
                        if row not in rightmost:
                            rightmost[row] = col
                        else:
                            rightmost[row] = max(col, rightmost[row])

            # Check if rock can move sideways
            if side == -1:
                for row, col in leftmost.items():
                    if col + side < 0:
                        can_move_sideways = False
                    elif grid[row][col + side] != ".":
                        can_move_sideways = False
            elif side == 1:
                for row, col in rightmost.items():
                    if col + side > 6:
                        can_move_sideways = False
                    elif grid[row][col + side] != ".":
                        can_move_sideways = False

            # Move rock sideways
            if can_move_sideways:

                # Reset old indices
                for row, col, rock in indices:
                    grid[row][col] = "."

                # Set new indices
                indices = [[row, col+side, rock] for row, col, rock in indices]
                for row, col, rock in indices:
                    grid[row][col] = rock

            # Check if rock can move down
            for row, col, rock in indices:
                if row == 0:
                    can_move_down = False
                elif rock == "@" and grid[row-1][col] != ".":
                    can_move_down = False

            # Exit condition, if rock is stuck
            if not can_move_down:
                #print("Stuck...\n")
                # Change the rock characters to # to distinguish from future rocks!
                for row, col, rock in indices:
                    grid[row][col] = "#"
                break

            # Move rock down
            # Reset old indices
            for row, col, rock in indices:
                grid[row][col] = "."

            # Set new indices:
            for row, col, rock in indices:
                grid[row-1][col] = rock

            # Remove empty air above rock in the grid 
            spaces = 0
            for row in grid[::-1]:
                if row == ["."]*7:
                    spaces += 1
                elif spaces > 0:
                    grid = grid[:-spaces]
                    break

        
        heights[current_rock + 1] = len(grid)
        unique = rock_type*len(jets) + jet
        if unique in uniques.keys():
            for old_pattern in uniques[unique].copy():
                if grid[-15:] == old_pattern["top_rows"]:
                    old_rock = old_pattern["rock"]
                    rocks_in_repetition = current_rock - old_rock
                    repetitions = (n_rocks - old_rock) // rocks_in_repetition
                    missing_rocks = n_rocks - old_rock - repetitions*rocks_in_repetition
                    initial_height = heights[old_rock]
                    diff_height = heights[current_rock] - heights[old_rock]
                    repeated_height = diff_height * repetitions
                    remaining_height = heights[old_rock + missing_rocks] - heights[old_rock]
                    return initial_height + repeated_height + remaining_height
                else:
                    uniques[unique].append({
                        "top_rows": grid[-15:],
                        "rock": current_rock
                    })
        else:
            uniques[unique] = [{
                "top_rows": grid[-15:],
                "rock": current_rock
            }]

    return heights[n_rocks]


if __name__ == "__main__":
    print(let_rocks_fall("test.txt", n_rocks=2022)) # 3068
    print(let_rocks_fall("test.txt", n_rocks=2022)) # 3141
    print(let_rocks_fall("test.txt", n_rocks=1_000_000_000_000)) # 1514285714288
    print(let_rocks_fall("test.txt", n_rocks=1_000_000_000_000)) # 1561739130391
