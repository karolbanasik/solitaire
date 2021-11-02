from pile import Pile
from discard_stack import DiscardStack
from row import Row
from discard_rule import DiscardRule


class Rule:
    def __init__(self, object_from, object_to, number_of_cards):
        self.object_from = object_from
        self.object_to = object_to
        self.number_of_cards = number_of_cards
        self.move_valid = True

    def check(self):
        if isinstance(self.object_to, Pile):
            self.validness_trap_switch(False)

        if isinstance(self.object_to, DiscardStack):
            rule = DiscardRule(self.object_from, self.object_to, self.number_of_cards)
            self.validness_trap_switch(rule.move_valid)

        if isinstance(self.object_to, Row):
            pass

        return self.move_valid

    def all_cards_must_face_up(self):
        card_on_back = self.object_from.cards[-self.number_of_cards]

    def validness_trap_switch(self, check_result):
        if self.move_valid:
            self.move_valid = check_result
