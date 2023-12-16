import numpy as np


def read_file(filename):
    valves = ["AA"]
    flow_rates = [0]
    leads_to = {}

    with open(filename, "r") as f:
        for line in f:
            words = line.split(" ")
            this_valve = words[1]
            flow_rate = int(words[4].replace("rate=", "").replace(";", ""))
            leads_to[this_valve] = [word.replace(",", "").replace("\n", "") for word in words[9:]]
            if flow_rate != 0:
                valves.append(this_valve)
                flow_rates.append(flow_rate)

    N = len(valves)
    travel_cost = [[0 for j in range(N)] for i in range(N)]

    for i in range(N):
        for j in range(i+1, N):
            # Find the cost of traveling from start to stop
            start = valves[i]
            stop = valves[j]

            valves_covered = leads_to[start].copy()
            cost = 2 # accounts for traveling to, and opening new valve

            # Crawl through caves
            while stop not in valves_covered:
                new_valves = []
                for valve in valves_covered:
                    new_valves += leads_to[valve].copy()
                valves_covered += set(new_valves)
                cost += 1

            travel_cost[i][j] = cost
            travel_cost[j][i] = cost

    return valves, flow_rates, travel_cost


def pressure_one_path(path, flow_rates, travel_cost, minutes=30):
    elapsed_minutes = 0
    pressure = 0
    valves_opened = 0
    total_flow_rate_of_open_valves = 0

    for i in range(len(path) - 1):
        at = path[i]
        to = path[i + 1]
        new_minutes = travel_cost[at][to]
        if elapsed_minutes + new_minutes < minutes:
            # There is time to go there and get benefit from opening this new valve
            elapsed_minutes += new_minutes
            valves_opened += 1
            total_flow_rate_of_open_valves += flow_rates[path[i + 1]]
            for j in range(i + 1):
                pressure += new_minutes*flow_rates[path[j]]

        else:
            # There is no time to go there, we can therefore only let time run out
            remaining_minutes = minutes - elapsed_minutes
            elapsed_minutes += remaining_minutes
            for j in range(i):
                pressure += remaining_minutes*flow_rates[path[j]]

            return pressure, False
        
    pressure += (minutes - elapsed_minutes)*total_flow_rate_of_open_valves

    return pressure, True


def total_pressure_released(
    valves, flow_rates, travel_cost, minutes=26
):
    N = len(valves)
    paths = [[0]]
    pressures = [0]

    for path in paths:
        valves_left = [i for i in range(1, N) if i not in path]
        if len(valves_left) == 0:
            break
        else:
            for idx in valves_left:
                new_path = path + [idx]
                pressure, used_all_valves = pressure_one_path(
                    new_path,
                    flow_rates,
                    travel_cost,
                    minutes=minutes
                )
                if used_all_valves:
                    paths.append(new_path)
                    pressures.append(pressure)

    return paths, pressures
    

if __name__ == "__main__":
    valves, flow_rates, travel_cost = read_file("test.txt")

    # Part 1, find most pressure released by one worker
    paths, pressures = total_pressure_released(
        valves,
        flow_rates,
        travel_cost,
        minutes=30,
    )
    max_pressure_human = max(pressures)
    print("Part 1:", max_pressure_human)

    # Part 2, find most pressure released by two workers
    paths, pressures = total_pressure_released(
        valves,
        flow_rates,
        travel_cost,
        minutes=26,
    )
    # pressures = np.array(pressures)
    idx = np.argsort(pressures)[::-1]
    max_pressure_human_and_elephant = 0
    top_N = len(paths) # for input, limit to ~200
    for i in range(top_N):
        for j in range(i, top_N):
            if all(valve not in paths[idx[i]][1:] for valve in paths[idx[j]][1:]):
                max_pressure_human_and_elephant = max(
                    max_pressure_human_and_elephant,
                    pressures[idx[i]] + pressures[idx[j]]
                )

    print("Part 2:", max_pressure_human_and_elephant)
