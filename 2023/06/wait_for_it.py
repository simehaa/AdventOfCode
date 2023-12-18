from math import ceil, floor, prod, sqrt


def read_input(filename):
    with open(filename) as f:
        lines = f.readlines()
        _, race_times = lines[0].split(":")
        _, record_distances = lines[1].split(":")
    return race_times, record_distances


def ways_to_win(race_time, record_distance):
    sq = sqrt(race_time**2 - 4*record_distance)
    if sq.is_integer():
        if ((race_time - sq)/2).is_integer():
            return floor(sq) - 1
        else:
            return floor(sq)
    else:
        low = floor((race_time - sq)/2)
        high = ceil((race_time + sq)/2)
        return high - low - 1


if __name__ == "__main__":
    for filename, solutions in zip(["test.txt", "test.txt"], [(288, 71503), (503424, 32607562)]):
        print(filename)
        race_times, record_distances = read_input(filename)
        part_1 = prod([ways_to_win(int(t), int(d)) for t, d in zip(race_times.split(), record_distances.split())])
        part_2 = ways_to_win(int(race_times.replace(" ", "")), int(record_distances.replace(" ", "")))
        print("Part 1:", part_1, part_1 == solutions[0])
        print("Part 2:", part_2, part_2 == solutions[1])
