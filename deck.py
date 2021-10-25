from card import Card
from card_rank import CardRank
from card_suit import CardSuit
import random


class Deck:
    def __init__(self):
        self.cards = []
        for rank_symbol in CardRank.ranks:
            for suit_name in CardSuit.suits:
                suit = CardSuit(suit_name)
                rank = CardRank(rank_symbol)
                card = Card(suit, rank)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def return_last_card(self, face_up=False):
        last_card = self.cards.pop(-1)
        last_card.face_up = face_up
        return last_card


if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()
    print('done')
