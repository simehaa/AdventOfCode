with open("input.txt", "r") as f:
    lines = f.readlines()
    _, race_times = lines[0].split(":")
    _, record_distances = lines[1].split(":")
    full_race_time = int(race_times.replace(" ", ""))
    full_record_distance = int(record_distances.replace(" ", ""))
    race_times = [int(t) for t in race_times.split()]
    record_distances = [int(d) for d in record_distances.split()]


def find_ways_to_win(time_, distance):
    different_ways_to_win = 0
    for i in range(1, time_+1):
        if i*(time_-i) > distance:
            different_ways_to_win += 1
    return different_ways_to_win

ways_to_win = 1
for race_time, record_distance in zip(race_times, record_distances):
    ways_to_win *= find_ways_to_win(race_time, record_distance)

print(ways_to_win)
print(find_ways_to_win(full_race_time, full_record_distance))
