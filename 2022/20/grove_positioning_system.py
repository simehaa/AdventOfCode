def read_input(filename):
    with open(filename) as f:
        return [eval(i) for i in f.readlines()]


def decrypt(encrypted_list, repeat=1):
    n = len(encrypted_list)
    idx_tracker = list(range(n))  # [0, 1, 2, 3, 4, 5]
    for i in idx_tracker.copy() * repeat:
        idx = idx_tracker.index(i)
        idx_tracker.pop(idx)
        idx_tracker.insert((idx + encrypted_list[i]) % len(idx_tracker), i)

    return [encrypted_list[idx] for idx in idx_tracker]


def extract_groove_coordinates(decrypted_list, indices=[1000, 2000, 3000], start_at=0):
    offset = decrypted_list.index(start_at)
    N = len(decrypted_list)
    coordinates = [decrypted_list[(i + offset) % N] for i in indices]
    return coordinates


if __name__ == "__main__":
    encrypted_list = read_input("test.txt")
    decrypted_list = decrypt(encrypted_list)
    coordinates = extract_groove_coordinates(decrypted_list)

    print(f"Part 1: {sum(coordinates)}")

    key = 811589153
    decrypted_list = decrypt([i * key for i in encrypted_list], repeat=10)
    coordinates = extract_groove_coordinates(decrypted_list)

    print(f"Part 2: {sum(coordinates)}")
