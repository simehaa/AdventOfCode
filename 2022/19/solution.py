import numpy as np

def read_input(filename):
    blueprints = []
    with open(filename, "r") as f:
        for line in f.readlines():
            words = line.split()
            blueprint = np.zeros((4, 4), dtype=np.int32)
            blueprint[0, 0] = int(words[6])
            blueprint[1, 0] = int(words[12])
            blueprint[2, 0] = int(words[18])
            blueprint[2, 1] = int(words[21])
            blueprint[3, 0] = int(words[27])
            blueprint[3, 2] = int(words[30])
            blueprints.append(blueprint)

    return blueprints


def simulate_buy_order(buy_order, blueprint, minutes=24):
    minerals = np.array([0, 0, 0, 0])
    robots = np.array([1, 0, 0, 0])
    purchase_number = 0
    for i in range(minutes):
        robots_copy = robots.copy()
        if purchase_number < len(buy_order):
            want_to_buy = buy_order[purchase_number]
            if np.all(minerals >= blueprint[want_to_buy]):
                minerals -= blueprint[want_to_buy]
                robots[want_to_buy] += 1
                purchase_number += 1
        minerals += robots_copy
    
    if purchase_number == len(buy_order):
        return minerals[3], True
    else:
        return minerals[3], False


# def simulate_buy_order(buy_order, blueprint, minutes=24):
#     minerals = np.array([0, 0, 0, 0])
#     robots = np.array([1, 0, 0, 0])
#     elapsed_minutes = 0

#     for robot in buy_order:
#         remaining_minutes = minutes - elapsed_minutes
#         robots_copy = robots.copy()
#         if purchase < len(buy_order):
#             want_to_buy = buy_order[purchase]
#             if np.all(minerals >= blueprint[want_to_buy]):
#                 minerals -= blueprint[want_to_buy]
#                 robots[want_to_buy] += 1
#                 purchase += 1
#         minerals += robots_copy
#     return minerals[3]

def find_maximum_geodes(blueprint, minutes=24):
    """
    minerals[0] and robots[0]: ore
    minerals[1] and robots[1]: clay
    minerals[2] and robots[2]: obsidian
    minerals[3] and robots[3]: geode
    """  
    max_geodes = 0
    # Initial buy orders
    buy_orders = [[0], [1]]

    for buy_order in buy_orders:
        if 3 in buy_order:
            geodes, used_full_buy_order = simulate_buy_order(buy_order, blueprint, minutes=minutes)
            max_geodes = max(max_geodes, geodes)
            if used_full_buy_order:
                continue
            else:
                buy_orders += [buy_order + [i] for i in range(1, 4)]
        elif 2 in buy_order:
            buy_orders += [buy_order + [i] for i in range(1, 4)]
        elif 1 in buy_order:
            buy_orders += [buy_order + [i] for i in range(3)]
        else:
            buy_orders += [buy_order + [i] for i in range(2)]
        print(f"\rNumber of buy_orders: {len(buy_orders)}", end="")
    
    return max_geodes


if __name__ == "__main__":  
    blueprints = read_input("test.txt")
    quality_level_sum = 0

    for i, bp in enumerate(blueprints):
        geodes = find_maximum_geodes(bp)
        print(f"Blueprint {i+1} opened {geodes} geodes")
        quality_level_sum += (i+1)*geodes
        exit()
        
    print(quality_level_sum)