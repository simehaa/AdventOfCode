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
        rx_low_pulse_counter = 0
        low_pulse_counter = 1
        high_pulse_counter = 0
        receivers = [("broadcaster", dest, "low") for dest in self.modules["broadcaster"]["destinations"]]
        for source, dest, pulse in receivers:
            # print(f"{source} -{pulse}-> {dest}")
            if pulse == "low":
                low_pulse_counter += 1
                if dest == "rx":
                    rx_low_pulse_counter += 1
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

        return low_pulse_counter, high_pulse_counter, rx_low_pulse_counter


PP = PulsePropagation("test.txt")
low_pulses = 0
high_pulses = 0
for i in range(1000):
    l, h, rx = PP.press_button()
    low_pulses += l
    high_pulses += h
print("Part 1:", low_pulses*high_pulses)

PP = PulsePropagation("test.txt")
i = 0
while True:
    i += 1
    l, h, rx = PP.press_button()
    print(f"\rrx={rx}, i={i}", end="")
    if rx == 1:
        print("Part 2:", i)
        break
