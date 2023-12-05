import re


directories = {}
with open("input.txt", "r") as f:
    path = []
    for line in f:
        cd_down = re.findall(r"\$ cd ([A-Za-z/]+)", line)
        cd_up = re.findall(r"\$ cd ..", line)
        ls = re.findall(r"\$ ls", line)
        if cd_down:
            path.append(cd_down[0])
            path_str = ""
            for d in path:
                if not path_str.endswith("/") and d != "/":
                    path_str += "/"
                path_str += d
            directories[path_str] = 0
        elif cd_up:
            path.pop()
        elif ls:
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


available_space = 70000000 - directories["/"]
needed_space = 30000000
at_most_100000_sum = 0
smallest_candidate = 0
for key, value in directories.items():
    # print(f"{key} {value}")
    if value <= 100000:
        at_most_100000_sum += value
    # Check if the directory is a candidate for the smallest directory
    if available_space + value >= needed_space:
        smallest_candidate = min(smallest_candidate, value) if smallest_candidate else value

print(at_most_100000_sum)
print(smallest_candidate)