import re

directories = {}
with open("test.txt") as f:
    path = []
    for line in f:
        cd_down = re.findall(r"\$ cd ([A-Za-z/]+)", line)
        if cd_down:
            path.append(cd_down[0])
            path_str = ""
            for d in path:
                if not path_str.endswith("/") and d != "/":
                    path_str += "/"
                path_str += d
            directories[path_str] = 0
        elif re.findall(r"\$ cd ..", line):
            path.pop()
        elif re.findall(r"\$ ls", line):
            pass
        else:
            a, b = line.split(" ")
            if a != "dir":
                path_str = ""
                for d in path:
                    if not path_str.endswith("/") and d != "/":
                        path_str += "/"
                    path_str += d
                    directories[path_str] += int(a)


at_most_100000_sum = 0
candidates = []
for key, value in directories.items():
    # print(f"{key} {value}")
    if value <= 100000:
        at_most_100000_sum += value
    # Check if the directory is a candidate for the smallest directory
    if 70000000 - directories["/"] + value >= 30000000:
        candidates.append(value)

print(f"Part 1: {at_most_100000_sum}")
print(f"Part 2: {min(candidates)}")
