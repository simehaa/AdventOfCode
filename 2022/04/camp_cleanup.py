overlap = 0
fully_contained = 0
with open("test.txt") as f:
    for line in f:
        elf1, elf2 = line.split(",")
        elf1 = elf1.split("-")
        elf2 = elf2.split("-")
        e1s = int(elf1[0])
        e1e = int(elf1[1])
        e2s = int(elf2[0])
        e2e = int(elf2[1])
        if (e2s >= e1s and e2s <= e1e) or (e1s >= e2s and e1s <= e2e):
            overlap += 1
            if e1s >= e2s and e1e <= e2e or e2s >= e1s and e2e <= e1e:
                fully_contained += 1


print("Part 1:", fully_contained)
print("Part 2:", overlap)
