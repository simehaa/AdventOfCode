from math import lcm


class PulsePropagation:
    def __init__(self, filename):
        self.modules = {}
        self.button_presses = 0
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
                    "state": False,
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
                if (
                    dest_properties["type"] == "conjunction"
                    and dest in source_properties["destinations"]
                ):
                    dest_properties["sources"][source] = False

    def press_button(self):
        conjunction_low_pulses = []
        self.button_presses += 1
        low_pulse_counter = 1
        high_pulse_counter = 0
        receivers = [
            ("broadcaster", dest, False) for dest in self.modules["broadcaster"]["destinations"]
        ]
        for source, dest, pulse in receivers:
            # print(f"{source} -{'on' if pulse else 'off'}-> {dest}")
            if not pulse:
                low_pulse_counter += 1
            elif pulse:
                high_pulse_counter += 1

            if dest not in self.modules:
                continue

            # Handle flip_flop module
            if self.modules[dest]["type"] == "flip_flop":
                if pulse:
                    continue
                send_pulse = not self.modules[dest]["state"]
                self.modules[dest]["state"] = send_pulse

            # Handle conjunction module
            elif self.modules[dest]["type"] == "conjunction":
                self.modules[dest]["sources"][source] = pulse
                send_pulse = not all(p for k, p in self.modules[dest]["sources"].items())
                if not send_pulse:
                    conjunction_low_pulses.append(dest)

            else:
                raise ValueError(f"unknown module type for {dest}")

            receivers += [
                (dest, new_dest, send_pulse) for new_dest in self.modules[dest]["destinations"]
            ]

        return low_pulse_counter, high_pulse_counter, conjunction_low_pulses


filename = "input.txt"
PP = PulsePropagation(filename)
low_pulses = 0
high_pulses = 0
conjunctions = {}
for i in range(10_000):
    l, h, cs = PP.press_button()
    if i < 1000:
        low_pulses += l
        high_pulses += h
    for c in cs:
        if c not in conjunctions:
            conjunctions[c] = PP.button_presses

print("Part 1:", low_pulses * high_pulses)
print("Part 2:", lcm(*conjunctions.values()))
