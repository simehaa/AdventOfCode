elf = 0
elf_calories = []
for line in open("test.txt"):
    if line.rstrip():
        elf += int(line)
    else:
        elf_calories.append(elf)
        elf = 0

print("Part 1:", max(elf_calories))
print("Part 2:", sum(sorted(elf_calories, reverse=True)[:3]))
