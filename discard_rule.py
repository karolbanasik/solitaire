from row import Row
from card import Card


class DiscardRule:
    def __init__(self, row_or_pile, discard_stack, number_of_cards):
        self.move_valid = True
        self.row_or_pile = row_or_pile
        self.discard_stack = discard_stack
        self.number_of_cards = number_of_cards

    def check(self):
        self.one_card_at_a_time()
        self.card_can_go_on_same_suit()

    def one_card_at_a_time(self):
        if self.number_of_cards != 1:
            self.validness_trap_switch(False)

    def card_can_go_on_same_suit(self):
        card = self.row_or_pile.cards[-1]
        suit_from = card.suit
        suit_to = self.discard_stack.cards[-1].suit
        self.validness_trap_switch(suit_from == suit_to)

    def validness_trap_switch(self, check_result):
        if self.move_valid:
            self.move_valid = check_result
