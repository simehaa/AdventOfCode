
modules = {}

for line in open("test.txt"):
    module, dest_modules = line.split(" -> ")
    modules[module] = dest_modules.rstrip().split(", ")
    
print(modules)

"""
flip-flop:
* startswith("%")
* initially OFF
* receives high pulse -> ignore
* receives low pulse:
    * if OFF, switch to ON, then send high pulse
    * if ON, switch to OFF, then send low pulse

conjunction:
* startswitch("&")
* remeber last pulse from each input module (initially low pulse for all)
* update memory
* if all memory is high pulses, send a low pulse
* else, send a high pulse

broadcast:
* relays an input pulse to all its destination modules

button:
* when pressed, send a low pulse to broadcast
"""