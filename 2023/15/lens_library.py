with open("test.txt") as f:
    sequence = f.readline().rstrip().split(",")

def HASMAP(step, current_value=0):
    for char in step:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value
    
print("Part 1:", sum([HASMAP(s) for s in sequence]))
    
boxes = {}
for i, step in enumerate(sequence):
    if "=" in step:
        label = step[:-2]
        box = HASMAP(label) 
        value = int(step[-1])
        if box in boxes:
            boxes[box][label] = value
        else:
            boxes[box] = {label: value}
    else:
        label = step[:-1]
        box = HASMAP(label)
        if box in boxes and label in boxes[box]:
            del boxes[box][label]
            if boxes[box] == {}:
                del boxes[box]

focus_power = 0
for box, lenses in boxes.items():
    for i, (key, focal_length) in enumerate(lenses.items()):
        focus_power += (box + 1) * (i + 1) * focal_length
print("Part 2:", focus_power)
