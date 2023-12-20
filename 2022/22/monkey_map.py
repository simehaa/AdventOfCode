class SurfaceWalker:
    def __init__(self,
        grid,
        actions,
        initial_coordinates=(0,50),
        boundary_condition="torus",
        side_length=50,
    ):
        """
        caridnal_direction: 'E', 'S', 'W', or 'N', initial direction
        boundary_condition: 'torus' or 'cube'
        """
        self.actions = actions
        self.grid = []
        for row in grid:
            self.grid.append([c for c in row])
        #self.grid[y][x] = "\033[38;2;255;100;100mX\033[0m"
        self.len_y = len(grid)
        self.len_x = len(grid[0])
        self.boundary_condition = boundary_condition
        self.coordinates = initial_coordinates
        self.facing = 0
        # Tables below should be indexed with self.facing%4
        self.cardinal_table = ["E", "S", "W", "N"]
        self.delta_table = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.facing_table = [0, 1, 2, 3]
        self.symbol_table = [">", "v", "<", "^"]
        # self.side stores the face at each coordinate
        N = side_length
        self.N = N
        self.side = []
        for y in range(4*N):
            row = []
            for x in range(3*N):
                if 0*N <= y < 1*N and 1*N <= x < 2*N:
                    side = 1
                elif 0*N <= y < 1*N and 2*N <= x < 3*N:
                    side = 2
                elif 1*N <= y < 2*N and 1*N <= x < 2*N:
                    side = 3
                elif 2*N <= y < 3*N and 0*N <= x < 1*N:
                    side = 4
                elif 2*N <= y < 3*N and 1*N <= x < 2*N:
                    side = 5
                elif 3*N <= y < 4*N and 0*N <= x < 1*N:
                    side = 6
                else:
                    side = 0
                row.append(side)
            self.side.append(row)
        self.color_counter = 0
        self.red = 0
        self.green = 0
        self.blue = 0

    def get_passwd(self):
        y, x = self.coordinates
        passwd = 1000*(y+1) + 4*(x+1) + self.facing
        return passwd

    def color_character(self, char):
        cycle = 6*128
        if self.color_counter % cycle < 128:
            self.red += 1
        elif self.color_counter % cycle < 2*128:
            self.red -= 1
        elif self.color_counter % cycle < 3*128:
            self.green += 1
        elif self.color_counter % cycle < 4*128:
            self.green -= 1
        elif self.color_counter % cycle < 5*128:
            self.blue += 1
        elif self.color_counter % cycle < 6*128:
            self.blue -= 1
        self.color_counter += 1
        return f"\033[38;2;{128+self.red};{128+self.green};{128+self.blue}m{char}\033[0m"

    def solve(self):
        for action in self.actions:
            if isinstance(action, int):
                for _ in range(action):
                    dy, dx = self.delta_table[self.facing]
                    y, x = self.coordinates
                    ny = (y + dy) % self.len_y
                    nx = (x + dx) % self.len_x

                    if self.boundary_condition == "torus":
                        while self.grid[ny][nx] == " ":
                            ny = (ny + dy) % self.len_y
                            nx = (nx + dx) % self.len_x
                        if self.grid[ny][nx] == "#":
                            break
                        elif self.grid[ny][nx] == ".":
                            self.coordinates = ny, nx
                    else:
                        """
                        .  1  2
                        .  3  .
                        4  5  .
                        6  .  .
                        """
                        if self.side[y][x] == self.side[ny][nx]:
                            if self.grid[ny][nx] == "#":
                                break
                            else:
                                self.coordinates = ny, nx
                                self.grid[ny][nx] = self.color_character(self.symbol_table[self.facing])
                        else:
                            N = self.N
                            sy = y % N
                            sx = x % N
                            if self.side[y][x] == 1:
                                ny = [sy, N, 3*N-sy-1, 3*N+sx][self.facing]
                                nx = [2*N, N+sx, 0, 0][self.facing]
                                new_facing = [0, 1, 0, 0][self.facing]
                            elif self.side[y][x] == 2:
                                ny = [3*N-sy-1, N+sx, sy, 4*N-1][self.facing]
                                nx = [2*N-1, 2*N-1, 2*N-1, sx][self.facing]
                                new_facing = [2, 2, 2, 3][self.facing]
                            elif self.side[y][x] == 3:
                                ny = [N-1, 2*N, 2*N, N-1][self.facing]
                                nx = [2*N+sy, N+sx, sy, N+sx][self.facing]
                                new_facing = [3, 1, 1, 3][self.facing]
                            elif self.side[y][x] == 4:
                                ny = [2*N+sy, 3*N, N-sy-1, N+sx][self.facing]
                                nx = [N, sx, N, N][self.facing]
                                new_facing = [0, 1, 0, 0][self.facing]
                            elif self.side[y][x] == 5:
                                ny = [N-sy-1, 3*N+sx, 2*N+sy, 2*N-1][self.facing]
                                nx = [3*N-1, N-1, N-1, N+sx][self.facing]
                                new_facing = [2, 2, 2, 3][self.facing]
                            elif self.side[y][x] == 6:
                                ny = [3*N-1, 0, 0, 3*N-1][self.facing]
                                nx = [N+sy, 2*N+sx, N+sy, sx][self.facing]
                                new_facing = [3, 1, 1, 3][self.facing]
                            else:
                                raise ValueError(f"Invalid side {self.side[y][x]}")
                            if self.grid[ny][nx] == "#":
                                break
                            else:
                                self.coordinates = ny, nx
                                self.facing = new_facing
                                self.grid[ny][nx] = self.color_character(self.symbol_table[self.facing])

            elif action == "R":
                self.facing = (self.facing + 1) % 4
            elif action == "L":
                self.facing = (self.facing - 1) % 4
            else:
                raise ValueError("Invalid action")
        
    def print_grid(self):
        for row in self.grid:
            for c in row:
                print(c, end="")
            print()


def read_file(filename="input.txt"):
    grid = []
    actions = []
    with open(filename) as f:
        for line in f:
            if "." in line or "#" in line:
                grid.append(line.rstrip())
            else:
                directions = f.readline()
    len_x = max([len(row) for row in grid])
    for j, row in enumerate(grid):
        if len(row) < len_x:
            grid[j] += (len_x - len(row)) * " "
    num = ""
    for c in directions:
        if c in ["R", "L"]:
            actions.append(int(num))
            actions.append(c)
            num = ""
        else:
            num += c
    if num:
        actions.append(int(num))
    return grid, actions


if __name__ == "__main__":
    grid, actions = read_file()
    Torus = SurfaceWalker(grid, actions, boundary_condition="torus")
    Torus.solve()
    Cube = SurfaceWalker(grid, actions, boundary_condition="cube")
    Cube.solve()
    Cube.print_grid()
    print("Part 1:", Torus.get_passwd())
    print("Part 2:", Cube.get_passwd())
