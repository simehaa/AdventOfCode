def get_elevation(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if letter in alphabet:
        return alphabet.index(letter)
    if letter == "S":
        return get_elevation("a")
    if letter == "E":
        return get_elevation("z")
    raise ValueError(f"Invalid letter: {letter}")


def find_shortest_path(grid, start, end_letter, ascend=True):
    # Find the shortest path
    paths = [[start]]
    shortest_path = []
    end_reached = False

    # Perform all possible moves (while limiting versions with same or more steps to any location)
    while not end_reached:
        new_paths = []
        for path in paths:
            for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                si = path[-1][0]
                sj = path[-1][1]
                di = si + direction[0]
                dj = sj + direction[1]

                # Check if at boundary
                if (
                    dj < 0
                    or dj >= width
                    or di < 0
                    or di >= height
                    or [di, dj] in path
                    or ascend
                    and get_elevation(grid[di][dj]) - 1 > get_elevation(grid[si][sj])
                    or not ascend
                    and get_elevation(grid[si][sj]) - 1 > get_elevation(grid[di][dj])
                ):
                    continue

                # Check if End is reached
                if grid[di][dj] == end_letter:
                    end_reached = True
                    shortest_path = path + [[di, dj]]
                    break

                # Add as a potential path
                # Check if this location is already reached by (1) a previous path or (2) one of the new paths
                for other_path in paths + new_paths:
                    if [di, dj] in other_path:
                        break
                else:
                    new_paths.append(path + [[di, dj]])
            else:
                continue
            break

        paths = new_paths

    return shortest_path


def plot_path(height, width, path):
    grid = [["." for _ in range(width)] for _ in range(height)]
    ei, ej = path[-1]
    grid[ei][ej] = "E"
    for s in range(len(path) - 1):
        si, sj = path[s]
        di, dj = path[s + 1]
        if di == si + 1:
            grid[si][sj] = "v"
        elif di == si - 1:
            grid[si][sj] = "^"
        elif dj == sj + 1:
            grid[si][sj] = ">"
        elif dj == sj - 1:
            grid[si][sj] = "<"

    for row in grid:
        print("".join(row))


if __name__ == "__main__":
    # Read input
    with open("test.txt") as f:
        grid = [[char for char in line if char != "\n"] for line in f]

    height = len(grid)
    width = len(grid[0])

    # Find the start
    for i in range(height):
        for j in range(width):
            if grid[i][j] == "S":
                start = [i, j]
            elif grid[i][j] == "E":
                end = [i, j]

    # Find shortest ascend from 'S' to 'E'
    shortest_path = find_shortest_path(grid, start, end_letter="E", ascend=True)
    print("Part 1:", len(shortest_path) - 1)

    # Find shortest path from any 'a' to 'E'
    # Analogous to finding shortes descend from 'E' to 'a'
    shortest_path = find_shortest_path(grid, end, end_letter="a", ascend=False)
    print("Part 2:", len(shortest_path) - 1)
