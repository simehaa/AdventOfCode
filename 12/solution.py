def get_elevation(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if letter in alphabet:
        return alphabet.index(letter)
    else:
        if letter == "S":
            return get_elevation("a")
        elif letter == "E":
            return get_elevation("z")
        else:
            raise ValueError(f"Invalid letter: {letter}")


def find_shortest_path(grid, start, end_letter, ascend=True):
    # Find the shortest path
    paths = [[start]]
    end_reached = False

    # Perform all possible moves (while limiting versions with same or more steps to any location)
    while not end_reached:
        new_paths = []
        for path in paths:
            if end_reached:
                break
            for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                si = path[-1][0]
                sj = path[-1][1]
                di = si + direction[0]
                dj = sj + direction[1]

                # Check if at boundary
                if dj < 0 or dj >= width or di < 0 or di >= height:
                    continue

                # We don't want to go back to anywhere on the current path to avoid infinite loops
                elif [di, dj] in path:
                    continue

                # Check if too steep
                elif ascend and get_elevation(grid[di][dj]) - 1 > get_elevation(grid[si][sj]):
                    continue

                elif not ascend and get_elevation(grid[si][sj]) - 1 > get_elevation(grid[di][dj]):
                    continue

                # Check if End is reached
                elif grid[di][dj] == end_letter:
                    end_reached = True
                    new_paths.append(path + [[di, dj]])
                    break

                # Add as a potential path
                else:
                    # Check if this location is already reached by (1) a previous path or (2) one of the new paths
                    another_path_found = False
                    for other_path in paths + new_paths:
                        if [di, dj] in other_path:
                            another_path_found = True
                            break
                    
                    if not another_path_found:
                        new_paths.append(path + [[di, dj]])

        paths = new_paths

    shortest_path = min(paths, key=len)
    return len(shortest_path) - 1


if __name__ == "__main__":
    # Read input
    with open("input.txt") as f:
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
    print(f"Shortest path from 'S' to 'E': {shortest_path}")

    # Find shortest path from any 'a' to 'E'
    # Analogous to finding shortes descend from 'E' to 'a'
    shortest_path = find_shortest_path(grid, end, end_letter="a", ascend=False)
    print(f"Shortest path from 'E' to any 'a': {shortest_path}")
