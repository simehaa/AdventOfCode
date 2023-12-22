from math import lcm


class PulsePropagation:
    def __init__(self, filename):
        self.modules = {}
        for line in open(filename):
            module, dest_modules = line.split(" -> ")
            if module.startswith("broadcaster"):
                self.modules[module] = {
                    "type": "broadcaster",
                    "destinations": dest_modules.rstrip().split(", "),
                }
            elif module.startswith("%"):
                self.modules[module[1:]] = {
                    "type": "flip_flop",
                    "state": "off",
                    "destinations": dest_modules.rstrip().split(", "),
                }
            elif module.startswith("&"):
                self.modules[module[1:]] = {
                    "type": "conjunction",
                    "sources": {},
                    "destinations": dest_modules.rstrip().split(", "),
                }
        for source, source_properties in self.modules.items():
            for dest, dest_properties in self.modules.items():
                if dest_properties["type"] == "conjunction" and dest in source_properties["destinations"]:
                    dest_properties["sources"][source] = "low"

    def press_button(self):
        low_pulse_counter = 1
        high_pulse_counter = 0
        receivers = [("broadcaster", dest, "low") for dest in self.modules["broadcaster"]["destinations"]]
        for source, dest, pulse in receivers:
            # print(f"{source} -{pulse}-> {dest}")
            if pulse == "low":
                low_pulse_counter += 1
            elif pulse == "high":
                high_pulse_counter += 1

            if dest not in self.modules:
                continue

            # Handle flip_flop module
            if self.modules[dest]["type"] == "flip_flop":
                if pulse != "low":
                    continue
                new_state, send_pulse = ("on", "high") if self.modules[dest]["state"] == "off" else ("off", "low")
                self.modules[dest]["state"] = new_state
        
            # Handle conjunction module
            elif self.modules[dest]["type"] == "conjunction" :
                self.modules[dest]["sources"][source] = pulse
                send_pulse = "low" if all(p == "high" for k, p in self.modules[dest]["sources"].items()) else "high"
                
            else:
                raise ValueError(f"unknown module type for {dest}")

            receivers += [(dest, new_dest, send_pulse) for new_dest in self.modules[dest]["destinations"]]

        return low_pulse_counter, high_pulse_counter
    
    def reset(self):
        for _, module in self.modules.items():
            if module["type"] == "flip_flop":
                module["state"] = "off"
            elif module["type"] == "conjunction":
                for s, p in module["sources"].items():
                    p = "off"


PP = PulsePropagation("input.txt")
low_pulses = 0
high_pulses = 0
for i in range(1000):
    l, h = PP.press_button()
    low_pulses += l
    high_pulses += h
print("Part 1:", low_pulses*high_pulses)

for name, module in PP.modules.items():
    if "rx" in module["destinations"]:
        break
sources = PP.modules[name]["sources"].keys()
periods = []
for source in sources:
    PP.reset()
    i = 0
    while True:
        PP.press_button()
        print(f"\rfinding periodicity of {source}, i={i}", end="")
        i += 1
        if PP.modules[name]["sources"][source] == "high":
            periods.append(i)
            break
    print("\n", i)
print("Part 2:", lcm(*periods))
