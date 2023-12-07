def readfile(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    return lines


class Hand:
    def __init__(self, cards, bid, joker=False) -> None:
        self.cards = cards
        self.bid = int(bid)
        self.joker = joker

    def get_type(self):
        if not self.joker:
            unique_cards = list(set(self.cards))
            if len(unique_cards) == 1:
                return "five of a kind"
            elif len(unique_cards) == 2:
                if self.cards.count(unique_cards[0]) == 4 or self.cards.count(unique_cards[1]) == 4:
                    return "four of a kind"
                else:
                    return "full house"
            elif len(unique_cards) == 3:
                if self.cards.count(unique_cards[0]) == 3 or self.cards.count(unique_cards[1]) == 3 or self.cards.count(unique_cards[2]) == 3:
                    return "three of a kind"
                else:
                    return "two pairs"
            elif len(unique_cards) == 4:
                return "one pair"
            else:
                return "high card"
            
    def get_type_rank(self):
        return [
            "high card",
            "one pair",
            "two pairs", 
            "three of a kind", 
            "full house", 
            "four of a kind", 
            "five of a kind", 
        ].index(self.get_type())
    
    def get_card_rank(self, card):
        if self.joker:
            return ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"].index(card)
        else:
            return ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"].index(card)

    def __gt__(self, other):
        if self.get_type_rank() > other.get_type_rank():
            return True
        elif self.get_type_rank() == other.get_type_rank():
            for this_card, other_card in zip(self.cards, other.cards):
                this_card_rank = self.get_card_rank(this_card)
                other_card_rank = self.get_card_rank(other_card)
                if this_card_rank == other_card_rank:
                    continue
                elif this_card_rank > other_card_rank:
                    return True
                else:
                    return False
        else:
            return False


def solve(lines, part=1):
    if part == 1:
        hands = []
        for line in lines:
            hand, bid = line.split()
            hands.append(Hand(hand, bid, joker=False))

        total_winnings = 0
        for i, hand in enumerate(sorted(hands)):
            rank = i + 1
            total_winnings += hand.bid * rank

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


# 32T3K 765 1
# KTJJT 220 2
# KK677 28 3
# T55J5 684 4
# QQQJA 483 5