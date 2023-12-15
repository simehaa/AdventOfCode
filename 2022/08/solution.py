grid = []

with open("test.txt", "r") as f:
    for line in f:
        row = []
        for c in line:
            if c != "\n":
                row.append(int(c))
        grid.append(row)

height = len(grid)
width = len(grid[0])

visible = 0
for i in range(height):
    for j in range(width):
        if i == 0 or i == height - 1 or j == 0 or j == width - 1:
            # Boundary
            visible += 1
        else:
            # Inside
            north = max([grid[i][j] for i in range(0,i)])
            south = max([grid[i][j] for i in range(i+1,height)])
            east = max([grid[i][j] for j in range(j+1,width)])
            west = max([grid[i][j] for j in range(0,j)])
            if grid[i][j] > north or grid[i][j] > south or grid[i][j] > east or grid[i][j] > west:
                visible += 1

print(f"Part 1: {visible}")


max_score = 0
best_position = [0, 0]
best_views_nsew = [0, 0, 0, 0]
for i in range(1, height - 1):
    for j in range(1, width - 1):
        tree = grid[i][j]
        north_tree, south_tree, east_tree, west_tree = 0, 0, 0, 0

        south_view = 1
        for south in range(i+1, height - 1):
            south_tree = grid[south][j]
            if south_tree < tree:
                south_view += 1
            else:
                break

        north_view = 1
        for north in range(i-1, 0, -1):
            north_tree = grid[north][j]
            if north_tree < tree:
                north_view += 1
            else:
                break

        east_view = 1
        for east in range(j+1, width - 1):
            east_tree = grid[i][east]
            if east_tree < tree:
                east_view += 1
            else:
                break
        
        west_view = 1
        for west in range(j-1, 0, -1):
            west_tree = grid[i][west]
            if west_tree < tree:
                west_view += 1
            else:
                break

        score = south_view * north_view * east_view * west_view
        if score > max_score:
            max_score = score
            best_views_nsew = [north_view, south_view, east_view, west_view]
            best_position = [i, j]


reasons = ["until the view is blocked"] * 4
if best_views_nsew[0] == best_position[0]:
    reasons[0] = f"all the way to the edge of the forest"
if best_views_nsew[1] == height - best_position[0] - 1:
    reasons[1] = f"all the way to the edge of the forest"
if best_views_nsew[2] == width - best_position[1] - 1:
    reasons[2] = f"all the way to the edge of the forest"
if best_views_nsew[3] == best_position[1]:
    reasons[3] = f"all the way to the edge of the forest"


print(f"Part 2: {max_score}")
