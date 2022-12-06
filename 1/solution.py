elf_calories = []
with open("input.txt", "r") as f:
    elf = 0
    for line in f:
        if line == "\n":
            elf_calories.append(elf)
            elf = 0
        else:
            elf += int(line)

# Part 1 - top 1 most hungry elf
print(max(elf_calories))

# Part 2 - sum of top 3 most hungry elves
print(sum(sorted(elf_calories, reverse=True)[:3]))