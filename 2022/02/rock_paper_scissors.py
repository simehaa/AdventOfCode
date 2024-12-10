def strategy1(opponent_move, my_move):
    lookup_table = {
        "A": "Rock",
        "B": "Paper",
        "C": "Scissors",
        "X": "Rock",
        "Y": "Paper",
        "Z": "Scissors",
    }
    my_shape = lookup_table[my_move]
    opponent_shape = lookup_table[opponent_move]
    score = shape_score[my_shape]
    if opponent_shape == my_shape:
        score += 3
    elif (
        opponent_shape == "Rock"
        and my_shape == "Paper"
        or opponent_shape == "Paper"
        and my_shape == "Scissors"
        or opponent_shape == "Scissors"
        and my_shape == "Rock"
    ):
        score += 6
    return score


def strategy2(opponent_move, my_move):
    lookup_table = {
        "A": "Rock",
        "B": "Paper",
        "C": "Scissors",
        "X": "Lose",
        "Y": "Draw",
        "Z": "Win",
    }

    opponent_shape = lookup_table[opponent_move]
    game_outcome = lookup_table[my_move]

    if game_outcome == "Draw":
        return 3 + shape_score[opponent_shape]
    if game_outcome == "Win":
        if opponent_shape == "Rock":
            return 6 + shape_score["Paper"]
        if opponent_shape == "Paper":
            return 6 + shape_score["Scissors"]
        if opponent_shape == "Scissors":
            return 6 + shape_score["Rock"]
    elif game_outcome == "Lose":
        if opponent_shape == "Rock":
            return shape_score["Scissors"]
        if opponent_shape == "Paper":
            return shape_score["Rock"]
        if opponent_shape == "Scissors":
            return shape_score["Paper"]


shape_score = {"Rock": 1, "Paper": 2, "Scissors": 3}

score_strategy1 = 0
score_strategy2 = 0
for line in open("test.txt"):
    opponent_move, my_move = line.split()
    score_strategy1 += strategy1(opponent_move[0], my_move[0])
    score_strategy2 += strategy2(opponent_move[0], my_move[0])

print("Part 1:", score_strategy1)
print("Part 2:", score_strategy2)
