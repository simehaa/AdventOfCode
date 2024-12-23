def read(filename):
    links = {}
    with open(filename) as f:
        for line in f.read().splitlines():
            a, b = line.split("-")
            if a in links:
                links[a].append(b)
            else:
                links[a] = [b]
            if b in links:
                links[b].append(a)
            else:
                links[b] = [a]
    return links


def get_triplets(links):
    triplets = set()
    for first, connections in links.items():
        for second in connections:
            for third in links[second]:
                if third in connections:
                    triplets.add(tuple(sorted([first, second, third])))
    return triplets


def get_num_triplets_with_t(triplets):
    total = 0
    for triplet in triplets:
        for computer in triplet:
            if computer.startswith("t"):
                total += 1
                break
    return total


def get_passwd(triplets, links):
    lan_party = []
    for triplet in triplets:
        group = list(triplet)
        for i, computer in enumerate(group):
            all_connections = links[computer]
            for contender in all_connections:
                if contender in group:
                    continue
                contenders_connections = links[contender]
                if all([c in contenders_connections for c in group]):
                    group.append(contender)
        if len(group) > len(lan_party):
            lan_party = group
    return ",".join(sorted(lan_party))


links = read("test.txt")
triplets = get_triplets(links)
print("part 1:", get_num_triplets_with_t(triplets))
print("part 2:", get_passwd(triplets, links))
