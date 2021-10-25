from card import Card
from card_rank import CardRank
from card_suit import CardSuit


class DiscardStack:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self):
        if len(self.cards) > 0:
            removed_card = self.cards.pop(-1)
            return removed_card

    def card_on_top(self):
        card_on_top = None
        if len(self.cards) == 0:
            return card_on_top
        else:
            card_on_top = self.cards[-1]
            return card_on_top


if __name__ == '__main__':
    print('a')
