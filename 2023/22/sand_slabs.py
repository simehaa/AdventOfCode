def read(filename):
    slabs = {}
    with open(filename) as f:
        for j, line in enumerate(f.readlines()):
            start, stop = line.strip().split("~")
            ax, ay, az = tuple(map(int, start.split(",")))
            bx, by, bz = tuple(map(int, stop.split(",")))
            if ax == bx and ay == by:
                slabs[j] = [(ax, ay, i) for i in range(min(az, bz), max(az, bz) + 1)]
            if ax == bx and az == bz:
                slabs[j] = [(ax, i, az) for i in range(min(ay, by), max(ay, by) + 1)]
            if az == bz and ay == by:
                slabs[j] = [(i, ay, az) for i in range(min(ax, bx), max(ax, bx) + 1)]
    return slabs


def get_id(coordinate, slabs):
    for i, slab in slabs.items():
        for other in slab:
            if coordinate == other:
                return i
    return None


def let_fall_one_step(slabs, all_positions):
    moved_slabs = set()  # slab id's that fell
    for i, slab in slabs.items():
        for x, y, z in slab:
            if (x, y, z - 1) in slab:
                continue
            if (x, y, z - 1) in all_positions or z == 1:
                break
        else:
            moved_slabs.add(i)
            new_slab = []
            for x, y, z in slab:
                new_slab.append((x, y, z - 1))
                all_positions.add((x, y, z - 1))
                all_positions.remove((x, y, z))
            slabs[i] = new_slab
    return slabs, all_positions, moved_slabs


def stabilize(slabs, all_positions):
    all_moved_slabs = set()
    while True:
        slabs, all_positions, moved_slabs = let_fall_one_step(slabs, all_positions)
        all_moved_slabs.update(moved_slabs)
        if not len(moved_slabs):
            break
    return slabs, all_positions, all_moved_slabs


def solve(slabs):
    all_positions = set()
    for i, slab in slabs.items():
        for x, y, z in slab:
            all_positions.add((x, y, z))
    slabs, all_positions, _ = stabilize(slabs, all_positions)
    # Find out which slabs can be disintegrated
    # Try to remove one slab, and simulate and record how many other
    # slabs moved
    num_safely = 0
    sum_chains = 0
    for i, slab in slabs.items():
        c_slabs = slabs.copy()
        c_all_positions = all_positions.copy()
        c_slabs.pop(i)
        for pos in slab:
            c_all_positions.remove(pos)
        _, _, chain = stabilize(c_slabs, c_all_positions)
        num_safely += not (len(chain))
        sum_chains += len(chain)

    print("Part 1:", num_safely)
    print("Part 2:", sum_chains)


solve(read("test.txt"))
solve(read("input.txt"))
