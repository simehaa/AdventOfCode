def sign(x):
    """Handy sign function, return sign of a number (-1, 0, 1)"""
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def move_rope(directions, steps, rope_length, height, width, start_x, start_y):
    """
    Move a rope of rope_length number of knots, through a grid of height x width,
    starting at start_x, start_y.

    Follow a specific movement pattern, given by directions and steps.

    Return the number of grid positions touched by rope's tail.
    """
    grid = [[0 for w in range(width)] for h in range(height)]

    # All knots should start at the same position
    knots = []
    for n in range(rope_length):
        knots.append([start_x, start_y])

    for d, s in zip(directions, steps):
        for step in range(s):

            # Move front knot (head)
            if d == "U":
                knots[0][0] -= 1
            elif d == "D":
                knots[0][0] += 1
            elif d == "L":
                knots[0][1] -= 1
            elif d == "R":
                knots[0][1] += 1
    
            for i in range(1, len(knots)):
                # Move following knot (tail)

                # If head is exactly one diagonaly step away, do nothing
                # H . H
                # . T .
                # H . H
                if abs(knots[i-1][0] - knots[i][0]) == 1 and abs(knots[i-1][1] - knots[i][1]) == 1:
                    pass

                # If head is exactly one adjacent step away, do nothing
                # . H .
                # H T H
                # . H .
                elif abs(knots[i-1][0] - knots[i][0]) + abs(knots[i-1][1] - knots[i][1]) == 1:
                    pass

                # If head is two steps directly up or down, move tail one step towards head
                # . . H . .
                # . . . . .
                # . . T . .
                # . . . . .
                # . . H . .
                elif abs(knots[i-1][0] - knots[i][0]) == 2 and knots[i-1][1] == knots[i][1]:
                    knots[i][0] += sign(knots[i-1][0] - knots[i][0])

                # If head is two steps directly left or right, move tail one step towards head
                # . . . . .
                # . . . . .
                # H . T . H
                # . . . . .
                # . . . . .
                elif abs(knots[i-1][1] - knots[i][1]) == 2 and knots[i-1][0] == knots[i][0]:
                    knots[i][1] += sign(knots[i-1][1] - knots[i][1])

                # If the head is a "knight move" away (last outcome, hence 'else'),
                # move tail diagonally towards head
                # . H . H .
                # H . . . H
                # . . T . .
                # H . . . H
                # . H . H .
                else:
                    knots[i][0] += sign(knots[i-1][0] - knots[i][0])
                    knots[i][1] += sign(knots[i-1][1] - knots[i][1])

            # Save tail's touchpoint position in grid
            grid[knots[-1][0]][knots[-1][1]] = 1

    # Count number of positions touched
    positions_touched = 0        
    for h in range(height):
        positions_touched += sum(grid[h])

    return positions_touched


if __name__ == "__main__":
    for r, part in zip([2, 10], [1, 2]):
        directions = []
        steps = []
        with open(f"test{part}.txt", "r") as f:
            for line in f:
                d, s = line.split()
                directions.append(d)
                steps.append(int(s))
        
        positions_touched = move_rope(directions, steps, r, 500, 500, 250, 250)
        print(f"Part {part}:", positions_touched)
