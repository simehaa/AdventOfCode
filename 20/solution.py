def read_input(filename):
    with open(filename, "r") as f:
        return [eval(i) for i in f.readlines()]
        
        
def decrypt(encrypted_list):
    n = len(encrypted_list)
    idx_tracker = list(range(n)) # [0, 1, 2, 3, 4, 5]
    for i in idx_tracker:
        idx = idx_tracker.index(i)
        elem = idx_tracker.pop(idx)
        pos = (encrypted_list[i] + idx) % len(idx_tracker)
        idx_tracker.insert(pos, i)
        encrypted_list = [encrypted_list[j] for j in idx_tracker]
        print(f"Popped {elem} from index {idx}, and re-inserted at index {pos}")
        print("after", [encrypted_list[j] for j in idx_tracker])
        print()
        # print([encrypted_list[idx] for idx in idx_tracker], "\n")

    # zero = idx_tracker.index(encrypted_list.index(0))


def extract_groove_coordinated(decrypted_list, indices=[1000, 2000, 3000], start_at=0):
    offset = decrypted_list.index(start_at)
    N = len(decrypted_list)
    coordinates = [decrypted_list[(i + offset) % N] for i in indices]
    return coordinates
       

if __name__ == "__main__":  
    encrypted_list = read_input("test.txt")
    decrypt(encrypted_list)
    #print(extract_groove_coordinated([1, 2, -3, 4, 0, 3, -2]))
