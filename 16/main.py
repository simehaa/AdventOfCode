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


def pressure_released(order, flow_rates, travel_cost, total_minutes=30):
    elapsed_minutes = 0
    pressure = 0
    valves_opened = 0
    total_flow_rate_of_open_valves = 0

    for i in range(len(order) - 1):
        at = order[i]
        to = order[i + 1]
        new_minutes = travel_cost[at][to]
        if elapsed_minutes + new_minutes < total_minutes:
            # There is time to go there and get benefit from opening this new valve
            elapsed_minutes += new_minutes
            valves_opened += 1
            total_flow_rate_of_open_valves += flow_rates[order[i + 1]]
            for j in range(i + 1):
                pressure += new_minutes*flow_rates[order[j]]

        else:
            # There is no time to go there, we can therefore only let time run out
            remaining_minutes = total_minutes - elapsed_minutes
            elapsed_minutes += remaining_minutes
            for j in range(i):
                pressure += remaining_minutes*flow_rates[order[j]]

            return pressure, False
        
    pressure += (total_minutes - elapsed_minutes)*total_flow_rate_of_open_valves

    return pressure, True


if __name__ == "__main__":
    valves, flow_rates, travel_cost = read_file("input.txt")
    N = len(valves)
    combinations = [[0]]
    pressures = [0]

    for comb in combinations:
        valves_left = [i for i in range(1, N) if i not in comb]
        if len(valves_left) == 0:
            break
        else:
            for idx in valves_left:
                new_combo = comb + [idx]
                pressure, used_all_valves = pressure_released(new_combo, flow_rates, travel_cost, total_minutes=26)
                if used_all_valves:
                    combinations.append(new_combo)
                    pressures.append(pressure)

    print(max(pressures))

    import numpy as np

    pressures = np.array(pressures)
    idx = np.argsort(pressures)[::-1]

    comb_pressure = []

    top_N = 1000
    for i in range(top_N):
        for j in range(i, top_N):
            human = combinations[idx[i]]
            elephant = combinations[idx[j]]
            unique = True
            for valve in human[1:]:
                if valve in elephant[1:]:
                    unique = False
                    break
            if unique:
                comb_pressure.append(pressures[idx[i]] + pressures[idx[j]])
            
    print(max(comb_pressure))
