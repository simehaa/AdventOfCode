import re


def solve(schematic):
    num_pattern = re.compile("\d+")
    gear_pattern = re.compile("\*")
    height = len(schematic)
    width = len(schematic[0])
    sum_of_part_numbers = 0
    sum_of_gear_ratios = 0

    for i, l in enumerate(schematic):
        for match in num_pattern.finditer(l):
            number = match.group()
            start = match.start()
            end = match.end()
            adjacent_symbol = False
            for x in range(max(0, i-1), min(height, i+2)):
                for y in range(max(0, start-1), min(width, end+1)):
                    if schematic[x][y] != "." and not schematic[x][y].isdigit():
                        adjacent_symbol = True        
            if adjacent_symbol:
                sum_of_part_numbers += int(number)

        for match in gear_pattern.finditer(l):
            number = match.group()
            start = match.start()
            end = match.end()
            matches = []
            for x in range(max(0, i-1), min(height, i+2)):
                for num in num_pattern.finditer(schematic[x][:]):
                    for pos in range(num.start(), num.end()):
                        if pos >= start-1 and pos <= start+1:
                            matches.append(int(num.group()))
                            break
            if len(matches) == 2:
                sum_of_gear_ratios += matches[0]*matches[1]
    return sum_of_part_numbers, sum_of_gear_ratios


schematic = [l.rstrip() for l in open("test.txt")]
solution_1, solution_2 = solve(schematic)
print("Part 1:", solution_1)
print("Part 2:", solution_2)
