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

def read_file():
    valves = {}
    with open("input.txt", "r") as f:
        for line in f:
            words = line.split(" ")
            valves[words[1]] = {
                "rate": int(words[4].replace("rate=", "").replace(";", "")), 
                "to": [word.replace(",", "").replace("\n", "") for word in words[9:]]
            }
    return valves


if __name__ == "__main__":
    valves = read_file()
    
    max_minutes = 30
    max_tunnel_visits = max_minutes // 2
    tunnel = "AA"
    valves.keys()
    unfinished_paths = [["startat AA"]]
    finished_paths = []
    done = False
    
    valves_with_flow = []
    for valve in valves:
        if valves[valve]["rate"] > 0:
            valves_with_flow.append(valve)

    first_valve_opened_at = {}    

    for i in range(29):
        print(f"{i+1}/30, paths: {len(unfinished_paths)}")
    
        new_paths = []

        for path in unfinished_paths:
            action, tunnel = path[-1].split(" ")
            next_tunnels = valves[tunnel]["to"].copy()

            # Avoid walking in loops
            tunnels_visited = []
            loop = False
            for step in path[::-1]:
                _action, _tunnel = step.split(" ")
                if _action == "open":
                    break
                else:
                    if _tunnel in tunnels_visited:
                        loop = True
                        break
                    else:
                        tunnels_visited.append(_tunnel)
            if loop:
                continue

            # Check how many valves have been opened in this path
            valves_opened = []
            for step in path:
                _action, _tunnel = step.split(" ")
                if _action == "open" and _tunnel not in valves_opened:
                    valves_opened.append(_tunnel)

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
            if tunnel not in valves_opened and valves[tunnel]["rate"] > 0:
                new_path = path + [f"open {tunnel}"]

                if len(valves_opened) == 0:
                    if tunnel not in first_valve_opened_at:
                        first_valve_opened_at[tunnel] = {"path": new_path}
                    elif len(new_path) >= len(first_valve_opened_at[tunnel]["path"]):
                        continue

                # Is this the last valve?
                if len(valves_opened) + 1 == len(valves_with_flow):
                    finished_paths.append(new_path)
                    continue
                
                # Otherwise, we continue this path
                else:
                    new_paths.append(new_path)

            

        unfinished_paths = new_paths
    finished_paths += unfinished_paths

    # Check how much pressure is released for each path
    most_pressure_released = 0
    for path in finished_paths:
        valves_opened = []
        pressure_released = 0

        for minute in range(1, max_minutes+1): # 1, 2, ..., 30
            for valve in valves_opened:
                pressure_released += valves[valve]["rate"]
            # print("minute", minute + 1, "pressure released:", pressure_released, end=" ")
            
            if minute < len(path):
                action, tunnel = path[minute].split(" ")
                if action == "open" and tunnel not in valves_opened:
                    valves_opened.append(tunnel)
                    # print("opened", tunnel, end=" ")
                elif action == "moveto":
                    pass
                    # print("move to", tunnel, end=" ")
            # print()
    
        most_pressure_released = max(most_pressure_released, pressure_released)

    print("most pressure released:", most_pressure_released)

        
