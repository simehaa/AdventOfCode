elf_calories = []
with open("test.txt", "r") as f:
    elf = 0
    for line in f:
        if line.rstrip():
            elf += int(line)
        else:
            elf_calories.append(elf)
            elf = 0

# Part 1 - top 1 most hungry elf
print("Part 1:", max(elf_calories))

# Part 2 - sum of top 3 most hungry elves
print("Part 2:", sum(sorted(elf_calories, reverse=True)[:3]))
