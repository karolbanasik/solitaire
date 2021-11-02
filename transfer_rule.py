
class TransferRule:
    def __init__(self, object_from, row_to, number_of_cards):
        self.number_of_cards = number_of_cards
        self.row_to = row_to
        self.object_from = object_from
        self.move_valid = True

    def colours_alternating(self):
        pass

    def younger_on_older(self):
        pass

    def king_on_empty(self):
        pass

    def transfer_to_empty_or_face_up(self):
        pass

    def validness_trap_switch(self, check_result):
        if self.move_valid:
            self.move_valid = check_result
