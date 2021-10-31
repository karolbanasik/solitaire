from pile import Pile
from discard_stack import DiscardStack
from row import Row


class Rule:
    def __init__(self, object_from, object_to, number_of_cards):
        self.object_from = object_from
        self.object_to = object_to
        self.number_of_cards = number_of_cards
        self.move_valid = True

    def check(self):
        if isinstance(self.object_to, Pile):
            self.move_valid = False
        if isinstance(self.object_to, DiscardStack):
            pass
        # TODO: subclass discard
        if isinstance(self.object_to, Row):
            pass
        # TODO: subclass row transfer

        return self.move_valid

    def all_cards_must_face_up(self):
        # TODO: work
        pass
