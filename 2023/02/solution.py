possible = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

sum_of_powers = 0
impossible_games = []
all_games = []
with open("input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        game_txt, cube_txt = line.split(":")
        _, game_id = game_txt.split(" ")
        game_id = int(game_id)
        all_games.append(game_id)
        sets_list = cube_txt.split(";")
    
        minimum = {
            "green": 0,
            "blue": 0,
            "red": 0,
        }
        for s in sets_list:
            cubes_list = s.split(",")
            for c in cubes_list:
                _, num, color = c.split(" ")
                num = int(num)
                if color.endswith("\n"):
                    color = color[:-1]
                if num > possible[color]:
                    impossible_games.append(game_id)
                if num > minimum[color]:
                    minimum[color] = num
        
        power = minimum["blue"]*minimum["green"]*minimum["red"]
        sum_of_powers += power
    
sum_of_possible_games = 0

for g in all_games:
    if g not in set(impossible_games):
        sum_of_possible_games += g

print(sum_of_possible_games)
print(sum_of_powers)