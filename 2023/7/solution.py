def readfile(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    return lines


def solve(lines, part=1):
    if part == 1:
        card_values = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
        high_cards = []
        hands = []
        bids = []
        ranks = [0]*len(lines)
        fives = []
        fours = []
        houses = []
        threes = []
        twos = []
        ones = []
        for i, line in enumerate(lines):
            hand, bid = line.split()
            hands.append(hand)
            bids.append(int(bid))
            cards = list(set(hand))

            # Check if the hand is something
            if len(set(hand)) == 1:
                fives.append(i)
            elif len(set(hand)) == 2:
                if hand.count(cards[0]) == 4 or hand.count(cards[1]) == 4:
                    fours.append(i)
                else:
                    houses.append(i)
            elif len(set(hand)) == 3:
                if hand.count(cards[0]) == 3 or hand.count(cards[1]) == 3 or hand.count(cards[2]) == 3:
                    threes.append(i)
                else:
                    twos.append(i)
            else:
                ones.append(i)


        # rank the fives based on the highest card
        max_rank = len(hands) + 1
        for hand_type in [fives, fours, houses, threes, twos, ones]:
            for i, this in enumerate(hand_type):
                better_than = 0
                for other in hand_type:
                    if this == other:
                        continue
                    for k in range(5):
                        this_card = hands[this][k]
                        other_card = hands[other][k]
                        this_card_rank = card_values.index(this_card)
                        other_card_rank = card_values.index(other_card)
                        if this_card_rank == other_card_rank:
                            continue
                        elif this_card_rank < other_card_rank:
                            better_than += 1
                        break
                
                ranks[this] = max_rank - len(hand_type) + better_than
            max_rank -= len(hand_type)
        
        if len(ranks) != len(set(ranks)):
            print("ERROR: duplicate ranks")
            exit(1)
        total_winnings = 0
        for b, r in zip(bids, ranks):
            total_winnings += b*r
   
        return total_winnings
    elif part == 2:
        return 0


def test_solve(part=1, test_solution=-1):
    test_result = solve(readfile("test.txt"), part=part)
    try:
        assert test_result == test_solution
    except AssertionError:
        print(f"Test for part {part} failed: {test_result} != {test_solution}")
    else:
        result = solve(readfile("input.txt"), part=part)
        print(f"Result for part {part}: {result}")

if __name__ == "__main__":
    test_solve(part=1, test_solution=6440)
    #test_solve(part=2, test_solution=-1)

# 250297448 too low