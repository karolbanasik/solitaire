from deck import Deck
from row import Row


class Table:
    rows = []
    pile = None
    discard_stack = [None] * 4

    def __init__(self, deck):
        deck.shuffle()
        for i in range(7):
            self.rows.append(Row())
        self.deal(deck)

    def deal(self, deck):
        for i in range(7):
            current_row = self.rows[i]
            current_row.cards.append(deck.return_last_card(face_up=True))
            if i + 1 != 7:
                for j in range(i + 1, 7):
                    current_row = self.rows[j]
                    current_row.cards.append(deck.return_last_card())
        self.pile = deck
        print('Done dealing')


if __name__ == '__main__':
    deck = Deck()
    table = Table(deck)
    print('Woohoo!')
