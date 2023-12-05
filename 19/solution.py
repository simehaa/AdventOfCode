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


def find_maximum_geodes(blueprint, minutes=24):
    """
    minerals[0] and robots[0]: ore
    minerals[1] and robots[1]: clay
    minerals[2] and robots[2]: obsidian
    minerals[3] and robots[3]: geode
    """

    geodes = 0
    buy_orders = [[0, 1], [1, 0], [1, 1], [0, 0]]
    # Generate possible buy order priorities
    for i in range(8):
        new_buy_orders = []
        for buy_order in buy_orders:
            new_buy_orders.append(buy_order + [0])
            new_buy_orders.append(buy_order + [1])
            if 1 in buy_order:
                new_buy_orders.append(buy_order + [2])
                if 2 in buy_order:
                    new_buy_orders.append(buy_order + [3])
        buy_orders = new_buy_orders   

    best_buy_order = []
    for buy_order in buy_orders:
        minerals = np.array([0, 0, 0, 0])
        robots = np.array([1, 0, 0, 0])
        purchase = 0
        for minute in range(1, minutes+1):
            robots_copy = robots.copy()
            if purchase < len(buy_order):
                want_to_buy = buy_order[purchase]
                if np.all(minerals >= blueprint[want_to_buy]):
                    minerals -= blueprint[want_to_buy]
                    robots[want_to_buy] += 1
                    purchase += 1
            
            minerals += robots_copy

        if minerals[3] > geodes:
            geodes = minerals[3]
            best_buy_order = buy_order[:purchase]
    
    print(best_buy_order)
    return geodes


if __name__ == "__main__":  
    blueprints = read_input("test.txt")
    quality_level_sum = 0

    for i, bp in enumerate(blueprints):
        # if i == 0:
        #     quality_level_sum += 9
        #     continue
        geodes = find_maximum_geodes(bp)
        print(f"Blueprint {i+1} opened {geodes} geodes")
        quality_level_sum += (i+1)*geodes
        
    print(quality_level_sum)