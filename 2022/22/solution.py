import numpy as np


class SurfaceWalker:
    def __init__(self,
        grid,
        initial_cardinal_direction="E",
        initial_coordinates=(0,50),
        boundary_condition="torus",
        side_length=50,
    ):
        """
        caridnal_direction: 'E', 'S', 'W', or 'N', initial direction
        boundary_condition: 'torus' or 'cube'
        """
        self.grid = grid
        self.len_y = len(grid)
        self.len_x = len(grid[0])
        self.cardinal_direction = initial_cardinal_direction
        self.boundary_condition = boundary_condition
        self.y, self.x = initial_coordinates
        self.cardinal_table = ["E", "S", "W", "N"]
        self.delta_table = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.facing_table = [0, 1, 2, 3]
        self.symbol_table = [">", "v", "<", "^"]
        self.N = side_length
        self.side = np.zeros((self.N*4, self.N*3))
        self.side[0*self.N:1*self.N, 1*self.N:2*self.N] = 1
        self.side[0*self.N:1*self.N, 2*self.N:3*self.N] = 2
        self.side[1*self.N:2*self.N, 1*self.N:2*self.N] = 3
        self.side[2*self.N:3*self.N, 0*self.N:1*self.N] = 4
        self.side[2*self.N:3*self.N, 1*self.N:2*self.N] = 5
        self.side[3*self.N:4*self.N, 0*self.N:1*self.N] = 6
        
    def symbol(self):
        return self.symbol_table[self.cardinal_table.index(self.cardinal_direction)]
    
    def delta(self):
        return self.delta_table[self.cardinal_table.index(self.cardinal_direction)]
    
    def facing(self):
        return self.facing_table[self.cardinal_table.index(self.cardinal_direction)]
    
    def rotate(self, rotations=1, direction="R"):
        """
        direction: "R" or "L"
        ticks: no. of rotation steps in direction
        """
        ticks = rotations if direction == "R" else -rotations
        i = self.cardinal_table.index(self.cardinal_direction)
        i = (i + ticks) % len(self.cardinal_table)
        self.cardinal_direction = self.cardinal_table[i]
    
    def get_passwd(self):
        passwd = 1000*(self.y+1) + 4*(self.x+1) + self.facing()
        return passwd
    
    def torus(self, steps):
        # dy and dx will stay constant because we will not
        # rotate during walking these steps in one direction
        dy, dx = self.delta()
        for j in range(steps):
            # Get new indices
            new_y = (self.y + dy) % self.len_y
            new_x = (self.x + dx) % self.len_x
            # If " " then we are outside the surface
            # and can keep walking until we wrap around to
            # the other side (while keeping direction and rotation)
            while grid[new_y][new_x] == " ":
                new_y = (new_y + dy) % self.len_y
                new_x = (new_x + dx) % self.len_x
            # If we hit "#" then stop without updating indices
            if grid[new_y][new_x] == "#":
                break
            # As long as the next location is "." we can update indices
            elif grid[new_y][new_x] == ".":
                self.y, self.x = new_y, new_x

    def cube(self, steps):
        """
        .  1  2
        .  3  .
        4  5  .
        6  .  .
        """
        for j in range(steps):
            dy, dx = self.delta()
            # Get new indices
            new_y = (self.y + dy) % self.len_y
            new_x = (self.x + dx) % self.len_x
            # Compare current 
            current_side = self.side[self.y, self.x]
            new_side = self.side[new_y, new_x]
            if current_side != new_side:
                side_x = self.x % self.N
                side_y = self.y % self.N
                if current_side == 1 and self.cardinal_direction == "N":
                    # Go to side 6 from west
                    new_y = 3*self.N + side_x
                    new_x = 0*self.N
                    new_rotations = 1
                elif current_side == 1 and self.cardinal_direction == "W":
                    # Go to side 4 from west
                    new_y = 2*self.N + (self.N - side_y)
                    new_x = 0*self.N
                    new_rotations = 2
                elif current_side == 2 and self.cardinal_direction == "N":
                    # Go to side 6 from south
                    new_y = 3*self.N + side_y
                    new_x = 0*self.N + side_x
                    new_rotations = 0
                elif current_side == 2 and self.cardinal_direction == "E":
                    pass
                elif current_side == 2 and self.cardinal_direction == "S":
                    pass
                elif current_side == 3 and self.cardinal_direction == "E":
                    pass
                elif current_side == 3 and self.cardinal_direction == "W":
                    pass
                elif current_side == 4 and self.cardinal_direction == "W":
                    pass
                elif current_side == 4 and self.cardinal_direction == "W":
                    pass
                elif current_side == 5 and self.cardinal_direction == "W":
                    pass
                elif current_side == 5 and self.cardinal_direction == "W":
                    pass
                elif current_side == 6 and self.cardinal_direction == "W":
                    pass
                elif current_side == 6 and self.cardinal_direction == "W":
                    pass
                elif current_side == 6 and self.cardinal_direction == "W":
                    pass
                else:
                    raise NotImplementedError(
                        f"Going from "
                    )
    
            # Can walk one step as normal
            if grid[new_y][new_x] == "#":
                break
            elif grid[new_y][new_x] == ".":
                self.y, self.x = new_y, new_x

    
    def walk(self, actions):
        for action in actions:
            if isinstance(action, int):
                if self.boundary_condition == "torus":
                    self.torus(action)
                elif self.boundary_condition == "cube":
                    self.cube(action)

            elif isinstance(action, str):
                self.rotate(direction=action)

def read_file(filename="input.txt"):
    grid = []
    actions = []
    with open("input.txt", "r") as f:
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
    SW = SurfaceWalker(grid, initial_coordinates=(0, 50), boundary_condition="torus")
    SW.walk(actions)
    print(SW.get_passwd())