import numpy as np


def read_input(filename):
    blueprints = []
    with open(filename) as f:
        for line in f.readlines():
            words = line.split()
            blueprint = np.zeros((4, 4), dtype=np.int64)
            blueprint[0, 0] = int(words[6])
            blueprint[1, 0] = int(words[12])
            blueprint[2, 0] = int(words[18])
            blueprint[2, 1] = int(words[21])
            blueprint[3, 0] = int(words[27])
            blueprint[3, 2] = int(words[30])
            blueprints.append(blueprint)
    return blueprints


def wait_minutes(blueprint, robots, minerals, build):
    wait = int(np.ceil((blueprint[build] - minerals)[robots != 0] / robots[robots != 0]).max()) + 1
    return max(wait, 1)


def find_maximum_geodes(blueprint, total_minutes=24):
    """
    Blueprint looks like this
    [ 4   0   0   0] (cost of building an ore robot)
    [ 2   0   0   0] (cost of building a clay robot)
    [ 3  14   0   0] (cost of building an obsidian robot)
    [ 2   0   7   0] (cost of building an geode robot)
    ore clay obs geo

    Optimizations:
    1. Never buy more of a robot type than the highest cost of its resource
    2. The last robot in the buy order is a geode robot
    3. If a build order's ideal scenario doesn't beat the current max_geodes,
        then don't continue that build order. With t minutes left:
        a) current number of geodes
        b) t * geode robots
        c) t*(t+1)/2 => (0, 1, 3, 6, 10, ...)
    """
    max_ore_robots = blueprint[:, 0].max()
    max_clay_robots = blueprint[:, 1].max() - 1
    max_obsidian_robots = blueprint[:, 2].max() - 1
    max_geodes = 0
    build_orders = [[0], [1]]
    # build_orders = [[1, 1, 1, 2, 1, 2, 3, 3]]
    for build_order in build_orders:
        # Simulate build order
        robots = np.array([1, 0, 0, 0], dtype=np.int32)
        minerals = np.array([0, 0, 0, 0], dtype=np.int32)
        minute = 0
        for build in build_order:
            wait = wait_minutes(blueprint, robots, minerals, build)
            minute += wait
            if minute < total_minutes:
                minerals += wait * robots - blueprint[build]
                robots[build] += 1
                # print("\nminute:", minute)
                # print("robots:", robots)
                # print("minerals:", minerals)
                # print("build:", build)
            else:
                break
        if minute >= total_minutes:
            continue

        # Now check if we want to continue branching on this build_order
        time_left = total_minutes - minute
        minerals += time_left * robots
        ideal_number_of_geodes = minerals[-1]
        ideal_number_of_geodes += time_left * robots[-1]
        ideal_number_of_geodes += int(time_left * (time_left + 1) / 2)
        if ideal_number_of_geodes < max_geodes:
            continue

        max_geodes = max(minerals[-1], max_geodes)

        if (
            robots[0] < max_ore_robots
            and minute + wait_minutes(blueprint, robots, minerals, 0) < total_minutes
        ):
            build_orders.append(build_order + [0])

        if (
            robots[1] < max_clay_robots
            and minute + wait_minutes(blueprint, robots, minerals, 1) < total_minutes
        ):
            build_orders.append(build_order + [1])

        if (
            robots[1] > 0
            and robots[2] < max_obsidian_robots
            and minute + wait_minutes(blueprint, robots, minerals, 2) < total_minutes
        ):
            build_orders.append(build_order + [2])

        if robots[2] > 0 and minute + wait_minutes(blueprint, robots, minerals, 3) < total_minutes:
            build_orders.append(build_order + [3])

    return max_geodes


if __name__ == "__main__":
    blueprints = read_input("input.txt")
    quality_level_sum = 0
    first_three_product = 1
    for i, bp in enumerate(blueprints):
        # quality_level_sum += (i+1)*find_maximum_geodes(bp, 24)
        if i < 3 and i < len(blueprints):
            first_three_product *= find_maximum_geodes(bp, 32)
    # print("Part 1:", quality_level_sum)
    print("Part 2:", first_three_product)
