def read_input(filename):
    with open(filename) as f:
        return [eval(line) for line in f]


def full_surface(filename):
    coordinates = read_input(filename)
    surface = 6*len(coordinates)
    for x0, y0, z0 in coordinates:
        for x1, y1, z1 in coordinates:
            if x0 == x1 and y0 == y1 and z0 - z1 == 1:
                surface -= 1
            if x0 == x1 and y0 == y1 and z0 - z1 == -1:
                surface -= 1
            if x0 == x1 and z0 == z1 and y0 - y1 == 1:
                surface -= 1
            if x0 == x1 and z0 == z1 and y0 - y1 == -1:
                surface -= 1
            if z0 == z1 and y0 == y1 and x0 - x1 == 1:
                surface -= 1
            if z0 == z1 and y0 == y1 and x0 - x1 == -1:
                surface -= 1

    return surface
            

def outer_surface(filename):
    coordinates = read_input(filename)
    xmin, ymin, zmin = 20, 20, 20
    xmax, ymax, zmax = 0, 0, 0
    for x0, y0, z0 in coordinates:
        xmin = min(xmin, x0-1)
        ymin = min(ymin, y0-1)
        zmin = min(zmin, z0-1)
        xmax = max(xmax, x0+1)
        ymax = max(ymax, y0+1)
        zmax = max(zmax, z0+1)

    air = [(xmin, ymin, ymax)]
    air_touching_coordinates = []
    for x,y,z in air:
        neighbors = [
            (x,y,z+1), # back
            (x,y,z-1), # front
            (x+1,y,z), # right
            (x-1,y,z), # left
            (x,y+1,z), # up
            (x,y-1,z), # down
        ]
        for xn,yn,zn in neighbors:
            if xn < xmin or xn > xmax or yn < ymin or yn > ymax or zn < zmin or zn > zmax or (xn,yn,zn) in air:
                continue
            elif (xn, yn, zn) in coordinates:
                if (xn, yn, zn) not in air_touching_coordinates:
                    air_touching_coordinates.append((xn, yn, zn))
            elif (xn, yn, zn) not in coordinates:
                if (xn,yn,zn) not in air:
                    air.append((xn, yn, zn))
    
    # for z in range(zmin, zmax+1):
    #     print(f"\nz={z}")
    #     for y in range(ymin, ymax+1):
    #         for x in range(xmin, xmax+1):
    #             if (x,y,z) in air_touching_coordinates:
    #                 print("@", end="")
    #             elif (x,y,z) in coordinates:
    #                 print("#", end="")
    #             elif (x,y,z) in air:
    #                 print(".", end="")
    #             else:
    #                 print(".", end="")
    #         print()

    surface = 0
    for x,y,z in air_touching_coordinates:
        neighbors = [
            (x,y,z+1), # back
            (x,y,z-1), # front
            (x+1,y,z), # right
            (x-1,y,z), # left
            (x,y+1,z), # up
            (x,y-1,z), # down
        ]
        for xn,yn,zn in neighbors:
            if (xn,yn,zn) in air:
                surface += 1
            
    return surface


if __name__ == "__main__":
    print(full_surface("test.txt")) # 64
    print(full_surface("test.txt")) # 3530
    print(outer_surface("test.txt")) # 58
    print(outer_surface("test.txt")) # 2000
