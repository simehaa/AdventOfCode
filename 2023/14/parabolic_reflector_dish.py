class ParabolicReflector:
    def __init__(self, filename) -> None:
        self.disc = []
        with open(filename) as f:
            for line in f.readlines():
                self.disc.append(list(line.rstrip()))
        self.height = len(self.disc)
        self.width = len(self.disc[0])

    def __repr__(self) -> str:
        string = ""
        for row in self.disc:
            string += "".join(row) + "\n"
        return string

    def tilt_in_one_direction(self, direction=(-1, 0)) -> None:
        moves = True
        while moves:
            moves = False
            for y in range(self.height):
                for x in range(self.width):
                    ny, nx = y, x
                    ny += direction[0]
                    nx += direction[1]
                    if (
                        ny >= 0 and ny < self.height
                        and nx >= 0 and nx < self.width
                        and self.disc[y][x] == "O"
                        and self.disc[ny][nx] == "."
                    ):
                            self.disc[ny][nx] = "O"
                            self.disc[y][x] = "."
                            moves = True
    
    def perform_full_tilt_cycle(self) -> None:
        self.tilt_in_one_direction(direction=(-1, 0))
        self.tilt_in_one_direction(direction=(0, -1))
        self.tilt_in_one_direction(direction=(1, 0))
        self.tilt_in_one_direction(direction=(0, 1))

    def load_on_north_beam(self) -> int:
        load = 0
        for y, row in enumerate(self.disc):
            load += (self.height - y) * sum([c == "O" for c in row])
        return load
    
    def find_load_after_billion_tilt_cycles(self, look_back=150, warm_up=300):
        loads = []
        repeated_loads = []
        repeated_signatures = []
        for cycle in range(warm_up):
            print(f"\rCycle {cycle}", end="")
            self.perform_full_tilt_cycle()
            loads.append(self.load_on_north_beam())
        for cycle in range(look_back):
            print(f"\rCycle {cycle+warm_up}", end="")
            self.perform_full_tilt_cycle()
            loads.append(self.load_on_north_beam())
            signature = tuple(loads[-look_back:])
            if signature in repeated_signatures:
                break
            else:
                repeated_signatures.append(signature)
                repeated_loads.append(loads[-1])
        print()
        repeat_after = len(repeated_signatures)
        print(repeat_after)
        remaining = (1_000_000_000 - warm_up - 1) % repeat_after
        return repeated_loads[remaining]


if __name__ == "__main__":
    PR = ParabolicReflector("test.txt")
    PR.tilt_in_one_direction(direction=(-1, 0))
    print("Part 1:", PR.load_on_north_beam())
    print("Part 2:", PR.find_load_after_billion_tilt_cycles())
