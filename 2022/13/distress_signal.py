def compare(left, right):
    # Check if both are ints
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        elif left > right:
            return False

    # Check if both are lists
    if isinstance(left, list) and isinstance(right, list):
        # Check if one of the lists ran out
        if len(left) == 0 and len(right) > 0:
            return True
        elif len(right) == 0 and len(left) > 0:
            return False
        elif len(left) == 0 and len(right) == 0:
            return "continue"
        else:
            # Begin checking the elements
            check = compare(left[0], right[0])
            if check == "continue":
                return compare(left[1:], right[1:])
            else:
                return check
    
    # Check if left is int and right is list
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)

    # Check if left is list and right is list
    elif isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])

    return "continue"
    

if __name__ == "__main__":
    left = []
    right = []

    with open("test.txt") as f:
        for i, line in enumerate(f):
            if i%3 == 0:
                left.append(eval(line))
            elif i%3 == 1:
                right.append(eval(line))

    sum_of_indices = 0
    index = 0
    for l,r in zip(left, right):
        index += 1
        if compare(l, r):
            sum_of_indices += index

    print("Part 1:", sum_of_indices)

    all_packets = left + right + [[[2]], [[6]]]
    n = len(all_packets)
    
    # Bubble sort, slow but sufficient
    for i in range(n):
        for j in range(i+1, n):
            if compare(all_packets[j], all_packets[i]):
                all_packets[i], all_packets[j] = all_packets[j], all_packets[i]

    # Evaluate distress signal, which is the product of the indices (counting from 1) of [[2]] and [[6]]
    distress_signal = (all_packets.index([[2]]) + 1) * (all_packets.index([[6]]) + 1)
    print("Part 2:", distress_signal)
