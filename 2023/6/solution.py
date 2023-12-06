from math import sqrt, ceil

with open("input.txt", "r") as f:
    lines = f.readlines()
    _, race_times = lines[0].split(":")
    _, record_distances = lines[1].split(":")

ways = lambda t, d: ceil(sqrt(t**2 - 4*d))

ways_to_win = 1
for race_time, record_distance in zip(race_times.split(), record_distances.split()):
    ways_to_win *= ways(int(race_time), int(record_distance))
print(ways_to_win)
print(ways(int(race_times.replace(" ", "")), int(record_distances.replace(" ", ""))))
