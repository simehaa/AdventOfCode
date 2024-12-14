def read(filename):
    bots = []
    with open(filename) as f:
        for l in f.readlines():
            _, pos, vel = l.split("=")
            x, y = eval(pos.split()[0])
            vx, vy = eval(vel)
            bots.append((x, y, vx, vy))
    return bots


def print_grid(positions, width=101, height=103):
    for y in range(height):
        for x in range(width):
            if (x, y) in positions:
                print("#", end="")
            else:
                print(".", end="")
        print()


def part1(bots, width, height, seconds):
    q = [0, 0, 0, 0]
    for bot in bots:
        x, y, vx, vy = bot
        x = (x + vx * seconds) % width
        y = (y + vy * seconds) % height
        left = x < width // 2
        right = x > width // 2
        up = y < height // 2
        down = y > height // 2
        if left and up:
            q[0] += 1
        if right and up:
            q[1] += 1
        if left and down:
            q[2] += 1
        if right and down:
            q[3] += 1
    return q[0] * q[1] * q[2] * q[3]


def part2(bots, width=101, height=103, seconds=100):
    for i in range(seconds):
        pos = []
        mean_x = 0
        mean_y = 0
        var_x = 0
        var_y = 0
        for bot in bots:
            x, y, vx, vy = bot
            x = (x + vx * i) % width
            y = (y + vy * i) % height
            pos.append((x, y))
            mean_x += x
            mean_y += y
        mean_x /= len(bots)
        mean_y /= len(bots)
        for x, y in pos:
            var_x += (x - mean_x) * (x - mean_x)
            var_y += (y - mean_y) * (y - mean_y)
        var_x /= len(bots)
        var_y /= len(bots)
        if var_x < 500 and var_y < 500:
            print_grid(pos)
            return i
    return None


bots = read("test.txt")
print("Part 1 (test):", part1(bots, 11, 7, 100))
bots = read("input.txt")
print("Part 1:", part1(bots, 101, 103, 100))
print("Part 2:", part2(bots, 101, 103, 7000))
