from math import sqrt, ceil, prod

with open("input.txt", "r") as f:
    lines = f.readlines()
    _, race_times = lines[0].split(":")
    _, record_distances = lines[1].split(":")

ways = lambda t, d: ceil(sqrt(t**2 - 4*d))
print("Part 1:", prod([ways(int(t), int(d)) for t, d in zip(race_times.split(), record_distances.split())]))
print("Part 2:", ways(int(race_times.replace(" ", "")), int(record_distances.replace(" ", ""))))
