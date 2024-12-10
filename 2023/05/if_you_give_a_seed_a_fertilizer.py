def read_input(filename):
    current_mapping = ""
    map_ranges = {}
    for line in open(filename):
        if line.startswith("seeds"):
            seeds = [int(seed) for seed in line[6:].split()]
        elif line.endswith("map:\n"):
            current_mapping, _ = line.split()
            continue
        elif current_mapping and line != "\n":
            dest, source, range_len = [int(i) for i in line.split()]
            source_min_max = (source, source + range_len)
            dest_min_max = (dest, dest + range_len)
            if current_mapping not in map_ranges:
                map_ranges[current_mapping] = {"source": [source_min_max], "dest": [dest_min_max]}
            else:
                map_ranges[current_mapping]["source"].append(source_min_max)
                map_ranges[current_mapping]["dest"].append(dest_min_max)
    return seeds, map_ranges


def get_location(seed, map_ranges):
    value = seed
    for _, ranges in map_ranges.items():
        for source, dest in zip(ranges["source"], ranges["dest"]):
            if value >= source[0] and value < source[1]:
                offset = value - source[0]
                value = dest[0] + offset
                break
    return value


def get_seed(location):
    value = location
    for _, ranges in map_ranges.items().__reversed__():
        for source, dest in zip(ranges["source"], ranges["dest"]):
            if value >= dest[0] and value < dest[1]:
                offset = value - dest[0]
                value = source[0] + offset
                break
    return value


seeds, map_ranges = read_input("test.txt")
print("Part 1:", min([get_location(seed, map_ranges) for seed in seeds]))
for location in range(5_000_000):
    seed = get_seed(location)
    for start, stop in zip(seeds[::2], seeds[1::2]):
        if seed >= start and seed < start + stop:
            print("Part 2:", location)
            exit()
