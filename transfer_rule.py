from card import Card
from card_rank import CardRank


class TransferRule:
    def __init__(self, object_from, row_to, number_of_cards):
        self.number_of_cards = number_of_cards
        self.row_to = row_to
        self.object_from = object_from
        self.move_valid = True
        self.bottom_transferred_card = self.object_from.cards[-self.number_of_cards]
        self.top_row_to_card = self.row_to.cards[-1]

    def check(self):
        if len(self.row_to.cards) > 0:
            self.colours_alternating()
            self.transfer_to_face_up()
            self.younger_on_older()
        else:
            self.king_on_empty()

    def colours_alternating(self):
        self.validness_trap_switch(self.bottom_transferred_card.colour != self.top_row_to_card.colour)

    def younger_on_older(self):
        bottom_transferred_index = CardRank.ranks.index(self.bottom_transferred_card.rank)
        top_row_index = CardRank.ranks.index(self.top_row_to_card.rank)
        is_younger_on_older = top_row_index  == bottom_transferred_index + 1
        self.validness_trap_switch(is_younger_on_older)

    def king_on_empty(self):
        pass

    def transfer_to_face_up(self):
        pass

    def validness_trap_switch(self, check_result):
        if self.move_valid:
            self.move_valid = check_result

if __name__ == '__main__':
    card_a = Card(suit= 'hearts', rank='K')
    card_b = Card(suit= 'spades', rank='Q')
    from row import Row
    row_a = Row()
    row_b = Row()
    row_a.cards.append(card_a)
    row_b.cards.append(card_b)
    TransferRule(row_b, row_a, 1).younger_on_older()
    pass