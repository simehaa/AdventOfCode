import time

# Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
solution = [
    "startat AA",
    "moveto DD", 
    "open DD", 
    "moveto CC", 
    "moveto BB", 
    "open BB", 
    "moveto AA", 
    "moveto II", 
    "moveto JJ", 
    "open JJ", 
    "moveto II", 
    "moveto AA", 
    "moveto DD", 
    "moveto EE", 
    "moveto FF", 
    "moveto GG", 
    "moveto HH",
    "open HH",
    "moveto GG",
    "moveto FF",
    "moveto EE",
    "open EE",
    "moveto DD",
    "moveto CC",
    "open CC",
]

def read_file(filename):
    valves = {}
    with open(filename, "r") as f:
        for line in f:
            words = line.split(" ")
            valves[words[1]] = {
                "rate": int(words[4].replace("rate=", "").replace(";", "")), 
                "to": [word.replace(",", "").replace("\n", "") for word in words[9:]]
            }
    return valves


def is_loop(path):
    tunnels_visited = []
    for step in path[::-1]:
        a, t = step.split(" ")
        if a in ["moveto", "startat"]:
            if t in tunnels_visited:
                return True
            else:
                tunnels_visited.append(t)
        else:
            return False
    return False


def pressure(path, valves):
    pressure_released = 0
    valves_open = []
    for minute in range(1, 31): # 1, 2, ..., 30
        for valve in valves_open:
            pressure_released += valves[valve]["rate"]
        
        if minute < len(path):
            action, tunnel = path[minute].split(" ")
            if action == "open" and tunnel not in valves_open:
                valves_open.append(tunnel)
    return pressure_released


def valves_opened(path):
    valves_open = []
    for step in path:
        _action, _tunnel = step.split(" ")
        if _action == "open" and _tunnel not in valves_open:
            valves_open.append(_tunnel)
    return valves_open


def visited_opened_and_current(path):
    valves_visited = []
    valves_open = []
    for step in path[:-1]:
        _action, _tunnel = step.split(" ")
        if _tunnel not in valves_visited:
            valves_visited.append(_tunnel)
        if _action == "open" and _tunnel not in valves_open:
            valves_open.append(_tunnel)
        
    a, t = path[-1].split(" ")

    string = "".join(sorted(valves_visited)) + "_" + "".join(sorted(valves_open)) + "_" + t
    return string


def walk_and_open_valves(filename):
    valves = read_file(filename)
    tunnel = "AA"
    valves.keys()
    unfinished_paths = [["startat AA"]]
    finished_paths = []
    done = False    
    first_valve_opened_at = {} 
    valves_with_flow = []
    for valve in valves:
        if valves[valve]["rate"] > 0:
            valves_with_flow.append(valve)

    for i in range(30):
        print(f"{i+1}/30, paths: {len(unfinished_paths)}")
        new_paths = []

        for path in unfinished_paths:
            action, tunnel = path[-1].split(" ")
            next_tunnels = valves[tunnel]["to"].copy()

            # Avoid walking in loops
            if is_loop(path):
                continue

            # Check how many valves have been opened in this path
            valves_open = valves_opened(path)

            if len(next_tunnels) > 1:
                try:
                    last_action, last_tunnel = path[-2].split(" ")
                    if last_action == "open":
                        # We don't want to go back to the previously visited tunnel, 
                        # unless we have no other options
                        second_last_action, second_last_tunnel = path[-3].split(" ")
                        if second_last_tunnel in next_tunnels:
                            next_tunnels.remove(second_last_tunnel)
                    elif last_action == "moveto" and last_tunnel in next_tunnels:
                        # Since we are on the move, we don't want to go back to the second last tunnel,
                        # unless we have no other options
                        next_tunnels.remove(last_tunnel)
                except:
                    pass
            
            # Propose the moves
            for move in next_tunnels:
                new_path = path + [f"moveto {move}"]
                new_paths.append(new_path)

            # Check if it is worth to open valve (not opened before and has flow)
            if tunnel not in valves_open and valves[tunnel]["rate"] > 0:
                new_path = path + [f"open {tunnel}"]

                if len(valves_open) == 0:
                    if tunnel not in first_valve_opened_at:
                        first_valve_opened_at[tunnel] = {"path": new_path}
                    elif len(new_path) >= len(first_valve_opened_at[tunnel]["path"]):
                        continue

                # Is this the last valve?
                if len(valves_open) + 1 == len(valves_with_flow):
                    finished_paths.append(new_path)
                    continue
                
                # Otherwise, we continue this path
                else:
                    new_paths.append(new_path)

        # Only keep the best path from each last position
        unfinished_paths = []
        paths_at_valve = {}
        puv = ""
        for path in new_paths:
            
            if not is_loop(path):
                uv = visited_opened_and_current(path)
                
                if uv not in paths_at_valve:
                    paths_at_valve[uv] = path
                
                # Check which is best
                elif pressure(path, valves) > pressure(paths_at_valve[uv], valves):
                    paths_at_valve[uv] = path

        for vo, path in paths_at_valve.items():
            unfinished_paths.append(path)
    
    most_pressure_released = 0
    for path in finished_paths + unfinished_paths:
        most_pressure_released = max(most_pressure_released, pressure(path, valves))

    return most_pressure_released


if __name__ == "__main__":
    # print(walk_and_open_valves("test.txt")) # 1651
    # print(walk_and_open_valves("input.txt")) # 1659
