import re


num_pattern = re.compile("\d+")
pattern = re.compile("\*")


filename = "input.txt"
grid = []
with open(filename, "r") as f:
    lines = f.readlines()
    for line in lines:
        grid.append(line.rstrip())


# N = len(grid)
# M = len(grid[0])
# sums = 0
# for i, l in enumerate(grid):
#     for match in pattern.finditer(l):

#         number = match.group()
#         start = match.start()
#         end = match.end()

#         adjacent_symbol = False
#         for x in range(i-1, i+1+1):
#             if x < 0 or x >= N:
#                 continue

#             for y in range(start-1, end+1):
#                 if y < 0 or y >= M:
#                     continue

#                 if grid[x][y] != "." and not grid[x][y].isdigit():
#                     adjacent_symbol = True        

#         if adjacent_symbol:
#             sums += int(number)

# print(sums)


N = len(grid)
M = len(grid[0])
sums = 0
for i, l in enumerate(grid):
    for match in pattern.finditer(l):

        number = match.group()
        start = match.start()
        end = match.end()

        power = 1
        matches = []

        # above 
        for x in range(i-1, i+2):
            if x < 0 or x >= N:
                continue
            for num in num_pattern.finditer(grid[x][:]):
                
                # Check if num is actually adjacent
                adj = False
                for pos in range(num.start(), num.end()):
                    if pos >= start-1 and pos <= start+1:
                        adj = True
                        matches.append(int(num.group()))
                        break
        
        if len(matches) == 2:
            sums += matches[0]*matches[1]

print(sums)
        
# Not 1133939