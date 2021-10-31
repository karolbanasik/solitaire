from row import Row
from card import Card

class DiscardRule:
    def __init__(self):
        self.move_valid = True

    def one_card_at_a_time(self, number_of_cards):
        if number_of_cards > 1:
            self.move_valid = False

    def card_can_go_on_same_suit(self, row_or_pile, discard_stack):

        card = row_or_pile.cards[-1]
        suit_from = card.suit
        suit_to = discard_stack.cards[-1].suit
        self.move_valid = suit_from == suit_to
