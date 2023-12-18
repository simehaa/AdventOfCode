import re
from itertools import chain

# rising lines
# I) y = x + b

# falling lines
# II) y = -x + c

# intercept of rising and falling lines
# a) Solve for x by injecting II) into I)
#    x + b = -x + c
#    x = (c - b) / 2
# b) solve for y by rewriting I) and injecting into II)
#    x = y - b
#    y = -(y - b) + c
#    y = (c + b) / 2

def solve(filename, part=1):
    row = 10 if filename == "test.txt" else 2_000_000
    max_coor = 20 if filename == "test.txt" else 4_000_000
    locations = range(0, 0)
    rising_lines = [] # b
    falling_lines = [] # c
    with open(filename, "r") as f:
        for line in f:
            x0, y0, x1, y1 = re.findall(r"-?\d+", line)
            x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)
            dist = abs(x1 - x0) + abs(y1 - y0)
            x_dist = dist - abs(row - y0)
            locations = chain(locations, range(x0-x_dist, x0+x_dist + 1))
            rising_lines.append(y0 - x0 + dist)
            rising_lines.append(y0 - x0 - dist)
            falling_lines.append(y0 + x0 + dist)
            falling_lines.append(y0 + x0 - dist)
    if part == 1:
        return len(set(locations)) - 1
    elif part == 2:
        cs = []
        bs = []
        for b0 in set(rising_lines):
            for b1 in set(rising_lines):
                if abs(b1 - b0) == 2: # y-axis intercept must differ by 2 (to fit a gap of 1 between them)
                    b = min(b0, b1) + 1 # middle line is then the lowest line + 1
                    bs.append(b)
        for c0 in set(falling_lines):
            for c1 in set(falling_lines):
                if abs(c1 - c0) == 2:
                    c = min(c0, c1) + 1
                    cs.append(c)
        
        # This approach is very fast, but prone to 
        # over-count for the small test case
        # However, likely to only provide one solution
        # for the bigger input
        solutions = []
        for i, b in enumerate(set(bs)):
            for j, c in enumerate(set(cs)):
                x = int((c - b) / 2)
                y = int((c + b) / 2)
                if x < max_coor and y < max_coor:
                    solutions.append(str(x*4_000_000 + y))

        if len(solutions) == 0:
            return "No solutions found"
        elif len(solutions) == 1:
            return solutions[0]
        else:
            return "multiple solutions found: " + ", ".join(solutions)


if __name__ == "__main__":
    print("Part 1:", solve("test.txt", part=1))
    print("Part 2:", solve("test.txt", part=2))
