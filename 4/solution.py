overlap = 0
fully_contained = 0
with open("input.txt", "r") as f:
    for line in f:
        elf1, elf2 = line.split(",")
        elf1 = elf1.split("-")
        elf2 = elf2.split("-")
        e1s = int(elf1[0])
        e1e = int(elf1[1])
        e2s = int(elf2[0])
        e2e = int(elf2[1])
        print(f"{e1s}-{e1e},{e2s}-{e2e}, ", end="")
        if (
            e2s >= e1s and e2s <= e1e 
        ) or (
            e1s >= e2s and e1s <= e2e 
        ):
            overlap += 1
            print(f"overlap, ", end="")
            if e1s >= e2s and e1e <= e2e:
                fully_contained += 1
                print(f"range 1 fully contained in range 2")
            elif e2s >= e1s and e2e <= e1e:
                fully_contained += 1
                print(f"range 2 fully contained in range 1")
            else:
                print(f"not fully contained")
        else:
            print(f"no overlap")


print("Fully contained:", fully_contained)
print("Overlap:", overlap)