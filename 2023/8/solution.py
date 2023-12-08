from math import lcm

def readfile(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    return lines


def solve(lines, part=1):
    if part == 1:
        left_right = lines[0].strip()
        nodes = {}
        for line in lines[2:]:
            node = line[0:3]
            left = line[7:10]
            right = line[12:15]
            nodes[node] = [left, right]
        current_position = "AAA"
        end_position = "ZZZ"
        steps = 0
        while current_position != end_position:
            turn = left_right[steps % len(left_right)]
            steps += 1
            left, right = nodes[current_position]
            if turn == "L":
                current_position = left
            elif turn == "R":
                current_position = right
        return steps
    elif part == 2:
        left_right = lines[0].strip()
        nodes = {}
        paths = []
        times = []
        for line in lines[2:]:
            node = line[0:3]
            left = line[7:10]
            right = line[12:15]
            nodes[node] = [left, right]
            if node.endswith("A"):
                paths.append(node)

        for i in range(len(paths)):
            steps = 0
            while True:
                turn = left_right[steps % len(left_right)]
                steps += 1
                left, right = nodes[paths[i]]
                if turn == "L":
                    paths[i] = left
                elif turn == "R":
                    paths[i] = right
                
                if paths[i].endswith("Z"):
                    # print(paths[i], "ended after", steps)
                    times.append(steps)
                    break
        return lcm(*times)


if __name__ == "__main__":
    print(solve(readfile("test.txt"), part=1))
    print(solve(readfile("input.txt"), part=1))
    print(solve(readfile("part2.txt"), part=2))
    print(solve(readfile("input.txt"), part=2))
