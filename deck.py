from card import Card
from card_rank import CardRank
from card_suit import CardSuit


class Deck:
    def __init__(self):
        self.cards = []
        for rank in CardRank.ranks:
            for suit in CardSuit.suits:
                card = Card(rank, suit)
                self.cards.append(card)


if __name__ == "__main__":
    deck = Deck()
    print(deck)
