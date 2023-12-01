import re
import time

locations = []
with open("input.txt", "r") as f:
    for line in f:
        sensor, beacon = line.split(":")
        x0 = int(re.findall(r"x=(-?\d+)", sensor)[0])
        y0 = int(re.findall(r"y=(-?\d+)", sensor)[0])
        x1 = int(re.findall(r"x=(-?\d+)", beacon)[0])
        y1 = int(re.findall(r"y=(-?\d+)", beacon)[0])
        dist = abs(x1 - x0) + abs(y1 - y0)
        y_dist = abs(2000000 - y0)
        x_dist = dist - y_dist
        locations += [i for i in range(x0 - x_dist, x0 + x_dist + 1)]

print(f"Number of locations where beacon cannot be: {len(set(locations))}")
