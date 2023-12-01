class Blizzard:
    def __init__(self, filename) -> None:
        self.get_grid_from_file(filename)

    def get_grid_from_file(self, filename):
        self.grid = []
        with open(filename, "r") as f:
            for line in f:
                self.grid.append([i for i in line.rstrip()])

    def __repr__(self):
        string = ""
        for row in self.grid:
            for char in row:
                string += char
            string += "\n"
        return string[:-1]
    
    def simulate(self, positions):
        paths = []


if __name__ == "__main__":
    B = Blizzard("test.txt")
    print(B)