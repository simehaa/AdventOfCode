def read_input(filename):
    with open(filename) as f:
        lines = f.readlines()
        current_mapping = ""
        map_ranges = {}
        for line in lines:
            if line.startswith("seeds"):
                seeds = [int(seed) for seed in line[6:].split()]
            
            elif line.endswith("map:\n"):
                current_mapping, _ = line.split()
                continue
            
            elif current_mapping and line != "\n":
                dest, source, range_len = [int(i) for i in line.split()]
                source_min_max = (source, source+range_len)
                dest_min_max = (dest, dest+range_len)
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


if __name__ == "__main__":
    seeds, map_ranges = read_input("test.txt")

    # Part 1
    print(min([get_location(seed, map_ranges) for seed in seeds])) # 993500720

    # Part 2
    import datetime
    start_time = datetime.datetime.now()
    for location in range(5_000_000):
        seed = get_seed(location)
        for start, stop in zip(seeds[::2], seeds[1::2]):
            if seed >= start and seed < start+stop:
                print(seed, location) # 4917124
                print(datetime.datetime.now()-start_time)
                exit()