from functools import cache


def numeric_keypad(last_button, next_button):
    buttons = [("7", "8", "9"), ("4", "5", "6"), ("1", "2", "3"), (None, "0", "A")]
    sy, sx, ey, ex = 0, 0, 0, 0
    for y, row in enumerate(buttons):
        for x, c in enumerate(row):
            if c == last_button:
                sy, sx = y, x
            if c == next_button:
                ey, ex = y, x
    dy, dx = ey - sy, ex - sx
    horizontal_arrows = "" if dx == 0 else " ><"[abs(dx) // dx] * abs(dx)
    vertical_arrows = "" if dy == 0 else " v^"[abs(dy) // dy] * abs(dy)
    if sx == 0 and ey == 3:
        return horizontal_arrows + vertical_arrows + "A"
    if sy == 3 and ex == 0:
        return vertical_arrows + horizontal_arrows + "A"
    if dx < 0:
        return horizontal_arrows + vertical_arrows + "A"
    return vertical_arrows + horizontal_arrows + "A"


@cache
def directional_keypad(last_button, next_button):
    if last_button == next_button:
        return ["A"]
    buttons = [(None, "^", "A"), ("<", "v", ">")]
    sy, sx, ey, ex = 0, 0, 0, 0
    for y, row in enumerate(buttons):
        for x, c in enumerate(row):
            if c == last_button:
                sy, sx = y, x
            if c == next_button:
                ey, ex = y, x
    paths = [[(sy, sx)]]
    finished_paths = []
    for path in paths:
        y, x = path[-1]
        dist = abs(y - ey) + abs(x - ex)
        for ny, nx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
            if not (0 <= ny < 2 and 0 <= nx < 3) or (ny, nx) == (0, 0) or (ny, nx) in path:
                continue
            if buttons[ny][nx] == next_button:
                finished_paths.append(path + [(ny, nx)])
                continue
            new_dist = abs(ny - ey) + abs(nx - ex)
            if new_dist < dist:
                paths.append(path + [(ny, nx)])

    arrows = {(-1, 0): "^", (0, 1): ">", (1, 0): "v", (0, -1): "<"}
    return [
        "".join(arrows[(ny - py, nx - px)] for (py, px), (ny, nx) in zip(path, path[1:])) + "A"
        for path in finished_paths
    ]


buttons = ["^", "A", "<", "v", ">"]
lengths = {}
sequences = {}
for x in buttons:
    for y in buttons:
        seqs = directional_keypad(x, y)
        lengths[(x, y)] = len(seqs[0])
        sequences[(x, y)] = seqs


@cache
def dfs(x, y, depth):
    if depth == 1:
        return lengths[(x, y)]
    opt = float("inf")
    for seq in sequences[(x, y)]:
        length = 0
        for nx, ny in zip("A" + seq, seq):
            length += dfs(nx, ny, depth - 1)
        opt = min(opt, length)
    return opt


def solve(codes, depth=25):
    total = 0
    for code in codes:
        length = 0
        for a, b in zip("A" + code, code):
            sequence = numeric_keypad(a, b)
            for x, y in zip("A" + sequence, sequence):
                length += dfs(x, y, depth)
        total += int(code[:-1]) * length
    return total


test = ["029A", "980A", "179A", "456A", "379A"]
puzzle = ["935A", "319A", "480A", "789A", "176A"]
print("(test):", solve(test, 2))
print("part 1:", solve(puzzle, 2))
print("part 2:", solve(puzzle, 25))
