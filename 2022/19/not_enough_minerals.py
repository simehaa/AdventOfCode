from math import ceil


def read_blueprints(filename):
    blueprints = []
    with open(filename) as f:
        for line in f.readlines():
            words = line.split()
            blueprints.append(
                [
                    [
                        [int(words[6]), 0, 0, 0],
                        [int(words[12]), 0, 0, 0],
                        [int(words[18]), int(words[21]), 0, 0],
                        [int(words[27]), 0, int(words[30]), 0],
                    ],
                    [
                        max(int(words[6]), int(words[12]), int(words[18]), int(words[27])),
                        int(words[21]),
                        int(words[30]),
                    ],
                ]
            )
    return blueprints


def dfs(blueprint, max_bots, inv, bots, minutes, cache):
    if minutes == 0:
        return inv[3]  # Return the number of geodes at the end

    key = (*inv, *bots, minutes)
    if key in cache:
        return cache[key]

    # Action 1: Do nothing for the remaining time
    geodes = inv[3] + bots[3] * minutes

    # Try to build 0=ore, 1=clay, 2=obsidian, 3=geodes
    for i, cost in enumerate(blueprint):
        # Prune: Only applicable for ore, clay, obsidian
        # We never need to produce more than max_buys[i] of these
        if i < 3 and bots[i] >= max_bots[i]:
            continue

        # To build robot i, check the wait time needed
        wait = 0
        for need, have, bot_count in zip(cost, inv, bots):
            if need > 0:
                # impossible to build this bot,
                # because it requires a bot we don't have
                if bot_count == 0:
                    break
                wait = max(wait, ceil((need - have) / bot_count))
        else:
            remaining = minutes - wait - 1
            if remaining <= 0:
                continue

            # Build the bot
            new_bots = bots[:]
            new_bots[i] += 1

            # Pay the price
            new_inv = [x + y * (wait + 1) for x, y in zip(inv, bots)]
            for k, c in enumerate(cost):
                new_inv[k] -= c

            # Prune 2:
            for k in range(3):
                # This is if we produce a bot every minute remaining (except last)
                # We don't need to keep more than that (except for geodes)
                # Thus increasing the chance of cache hits
                max_resources = max_bots[k] * remaining - bots[k] * (remaining - 1)
                new_inv[k] = min(new_inv[k], max_resources)

            geodes = max(geodes, dfs(blueprint, max_bots, new_inv, new_bots, remaining, cache))

    cache[key] = geodes
    return geodes


if __name__ == "__main__":
    blueprints = read_blueprints("input.txt")
    q = 0
    for i, bp in enumerate(blueprints):
        bp, mb = bp
        g = dfs(bp, mb, [0, 0, 0, 0], [1, 0, 0, 0], 24, {})
        q += (i + 1) * g
    print("Part 1:", q)

    t = 1
    for i, bp in enumerate(read_blueprints("input.txt")):
        if i == 3:
            break
        bp, mb = bp
        g = dfs(bp, mb, [0, 0, 0, 0], [1, 0, 0, 0], 32, {})
        print("Blueprint", i + 1, "produces", g, "geodes")
        t *= g
    print("Part 2:", t)
