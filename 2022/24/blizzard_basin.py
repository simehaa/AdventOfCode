class Blizzard:
    def __init__(self, filename) -> None:
        self.get_grid_from_file(filename)
        self.height = len(self.grid)
        self.width = len(self.grid[0])
        self.start = (0, 1)
        self.end = (self.height-1, self.width-2)
        self.north_blizzards = []
        self.south_blizzards = []
        self.east_blizzards = []
        self.west_blizzards = []
        for y in range(1, self.height-1):
            for x in range(1, self.width-1):
                if self.grid[y][x] == "^":
                    self.north_blizzards.append((y, x))
                elif self.grid[y][x] == "v":
                    self.south_blizzards.append((y, x))
                elif self.grid[y][x] == ">":
                    self.east_blizzards.append((y, x))
                elif self.grid[y][x] == "<":
                    self.west_blizzards.append((y, x))
                
    def get_grid_from_file(self, filename):
        self.grid = []
        with open(filename, "r") as f:
            for line in f:
                self.grid.append([i for i in line.rstrip()])

    def __repr__(self):
        string = ""
        for y in range(self.height):
            for x in range(self.width):
                if (y, x) == self.start or (y, x) == self.end:
                    char = "."
                elif y == 0 or y == self.height - 1 or x == 0 or x == self.width - 1:
                    char = "#"
                else:
                    char = "."
                    number_of_blizzards = 0
                    if (y, x) in self.north_blizzards:
                        number_of_blizzards += 1
                        char = "^"
                    if (y, x) in self.south_blizzards:
                        number_of_blizzards += 1
                        char = "v"
                    if (y, x) in self.east_blizzards:
                        number_of_blizzards += 1
                        char = ">"
                    if (y, x) in self.west_blizzards:
                        number_of_blizzards += 1
                        char = "<"
                    if number_of_blizzards > 1:
                        char = str(number_of_blizzards)
                    elif number_of_blizzards == 0:
                        char = "."
                string += char
            string += "\n"
        return string[:-1]
    
    def simulate(self, start, goal):
        paths = [[start]]
        reached_end = False
        while not reached_end:
            self.north_blizzards = [((y-1-1)%(self.height-2)+1, x) for y, x in self.north_blizzards]
            self.south_blizzards = [((y+1-1)%(self.height-2)+1, x) for y, x in self.south_blizzards]
            self.east_blizzards = [(y, (x+1-1)%(self.width-2)+1) for y, x in self.east_blizzards]
            self.west_blizzards = [(y, (x-1-1)%(self.width-2)+1) for y, x in self.west_blizzards]
            new_paths = []
            for path in paths.copy():
                y, x = path[-1]
                moves = [
                    (y, x),
                    (y-1, x),
                    (y+1, x),
                    (y, x-1),
                    (y, x+1),
                ]
                for yn, xn in moves:
                    if (yn, xn) == goal:
                        reached_end = True
                        shortest_path = path + [(yn, xn)]
                    elif (
                        (yn, xn) not in self.north_blizzards 
                        and (yn, xn) not in self.south_blizzards
                        and (yn, xn) not in self.east_blizzards
                        and (yn, xn) not in self.west_blizzards
                        and yn > 0 and yn < self.height-1 
                        and xn > 0 and xn < self.width-1
                    ) or (yn, xn) == start:
                        for other_path in new_paths:
                            if (yn, xn) == other_path[-1]:
                                break
                        else:
                            new_paths.append(path + [(yn, xn)])
            paths = new_paths
        return len(shortest_path[1:])

if __name__ == "__main__":
    B = Blizzard("test.txt")
    first_trip = B.simulate(start=B.start, goal=B.end)
    print("Part 1:", first_trip)
    return_for_snacks = B.simulate(start=B.end, goal=B.start)
    last_trip = B.simulate(start=B.start, goal=B.end)
    print("Part 2:", first_trip + return_for_snacks + last_trip)
