import re
import time

# rising lines
# I) y = x + b

# falling lines
# II) y = -x + c

# intercept of rising and falling lines
# a) Solve for x by injecting II) into I)
#    x + b = -x + c
#    x = (c - b) / 2
# b) solve for y by rewriting I) and injecting into II)
#    x = y - b
#    y = -(y - b) + c
#    y = (c + b) / 2

start = time.time()
rising_lines = [] # b
falling_lines = [] # c
with open("input.txt", "r") as f:
    for line in f:
        sensor, beacon = line.split(":")
        x0 = int(re.findall(r"x=(-?\d+)", sensor)[0])
        y0 = int(re.findall(r"y=(-?\d+)", sensor)[0])
        x1 = int(re.findall(r"x=(-?\d+)", beacon)[0])
        y1 = int(re.findall(r"y=(-?\d+)", beacon)[0])
        dist = abs(x1 - x0) + abs(y1 - y0)
        rising_lines.append(y0 - x0 + dist)
        rising_lines.append(y0 - x0 - dist)
        falling_lines.append(y0 + x0 + dist)
        falling_lines.append(y0 + x0 - dist)

for b0 in set(rising_lines):
    for b1 in set(rising_lines):
        if abs(b1 - b0) == 2: # y-axis intercept must differ by 2 (to fit a gap of 1 between them)
            b = min(b0, b1) + 1 # middle line is then the lowest line + 1

for c0 in set(falling_lines):
    for c1 in set(falling_lines):
        if abs(c1 - c0) == 2:
            c = min(c0, c1) + 1

x = int((c - b) / 2)
y = int((c + b) / 2)
print(f"Coordinate ({x}, {y}): tuning frequency {x*4000000 + y}")
print(f"Time: {(time.time() - start)*1000:1.2f} ms")

assert x*4000000 + y == 12413999391794
