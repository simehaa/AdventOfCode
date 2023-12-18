from math import lcm


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


print("Part 1:", solve(list(open("test_1.txt")), part=1))
print("Part 2:", solve(list(open("test_2.txt")), part=2))