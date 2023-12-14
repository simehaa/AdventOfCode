def readfile(filename):
    disc = []
    with open(filename, "r") as f:
        for line in f.readlines():
            disc.append(list(line.rstrip()))
    return disc


def print_disc(disc):
    for row in disc:
        print("".join(row))
    print()


def tilt_disc(disc, direction=(-1, 0)):
    height = len(disc)
    width = len(disc[0])
    moves = True

    if direction[0]:
        while moves:
            moves = False
            y_range = range(0, height, 1) if direction[0] == -1 else range(height-1, -1, -1)
            for y in y_range:
                for x in range(width):
                    if disc[y][x] == "O":
                        ny, nx = y, x
                        ny += direction[0]
                        nx += direction[1]
                        if ny >= 0 and ny < height and disc[ny][nx] == ".":
                            disc[ny][nx] = "O"
                            disc[y][x] = "."
                            moves = True

    else:
        while moves:
            moves = False
            x_range = range(0, width, 1) if direction[1] == -1 else range(width-1, -1, -1)
            for x in x_range:
                for y in range(height):
                    if disc[y][x] == "O":
                        ny, nx = y, x
                        ny += direction[0]
                        nx += direction[1]
                        if nx >= 0 and nx < len(disc[0]) and disc[ny][nx] == ".":
                            disc[ny][nx] = "O"
                            disc[y][x] = "."
                            moves = True

    return disc


def load_on_north(disc):
    load = 0
    for y, row in enumerate(disc):
        for char in row:
            if char == "O":
                load += len(disc)-y
    return load


def tilt_cycle(disc):
    for i in range(4):
        disc = tilt_disc(disc, direction=[(-1, 0), (0, -1), (1, 0), (0, 1)][i%4])
    return disc


if __name__ == "__main__":
    disc = readfile("input.txt")
    print("Part 1:", load_on_north(tilt_disc(disc.copy())))

    loads = []
    warm_up = 500
    for cycle in range(warm_up):
        print(f"\rWarm up {cycle+1}", end="")
        disc = tilt_cycle(disc)
        loads.append(load_on_north(disc))
    print()

    signatures = {}
    look_back = 150
    for cycle in range(1000):
        print(f"\rContinuing {cycle+warm_up+1}", end="")
        disc = tilt_cycle(disc)
        loads.append(load_on_north(disc))

        signature = tuple(loads[-look_back:])
        if signature in signatures:
            break
        else:
            signatures[signature] = (cycle+warm_up+1, loads[-1])

    print()
    loads = []
    for key, value in signatures.items():
        c, l = value
        loads.append(l)

    repeat_after = len(signatures)
    remaining = (1_000_000_000 - warm_up - 1) % repeat_after
    print("Repeat pattern after", repeat_after, "cycles")
    print("Warm up of", warm_up, "cycles")
    repetitions = (1_000_000_000 - warm_up - 1) // repeat_after
    print("After warm up, need", repetitions, "repetitions")
    print("which gets us to cycle", warm_up+1+repetitions*repeat_after)
    print("the remainder of", remaining, "should get us to", 1000000000)
    print("And then the load is", loads[remaining])
