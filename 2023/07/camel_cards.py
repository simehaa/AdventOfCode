class Hand:
    def __init__(self, cards, bid, joker=False) -> None:
        self.cards = cards
        self.bid = int(bid)
        self.joker = joker

    def get_type(self):
        unique_cards = list(set(self.cards))
        if not self.joker or "J" not in unique_cards:
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
        else:
            if len(unique_cards) <= 2:
                return "five of a kind"
            elif len(unique_cards) == 3:
                if self.cards.count("J") in [2, 3]:
                    return "four of a kind"
                elif self.cards.count(unique_cards[0]) == 3 or self.cards.count(unique_cards[1]) == 3 or self.cards.count(unique_cards[2]) == 3:
                    return "four of a kind"
                else:
                    return "full house"
            elif len(unique_cards) == 4:
                return "three of a kind"
            else:
                return "one pair"
            
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


def solve(lines, joker=False):
    hands = [Hand(*l.split(), joker=joker) for l in lines]
    total_winnings = 0
    for i, hand in enumerate(sorted(hands)):
        total_winnings += hand.bid * (i + 1)
    return total_winnings


lines = list(open("test.txt"))
print("Part 1:", solve(lines, joker=False))
print("Part 2:", solve(lines, joker=True))
