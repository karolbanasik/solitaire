from card import Card
from row import Row

class Move:
    def __init__(self):
        self.valid = True

    def transfer_between_rows(self, row_from, row_to, card_count):
        cards_to_be_taken = self._take_cards_from_row(row_from, card_count)
        if cards_to_be_taken is None:
            return None
        bottom_transferred_card = cards_to_be_taken[0]
        if len(row_to.cards) == 0:
            if bottom_transferred_card.symbol == 'K':
                row_to.append(cards_to_be_taken)
                return None
            else:
                self.valid = False
                return None

        top_row_card = row_to.cards[-1]
        if not top_row_card.face_up:
            self.valid = False
            return None

        if self._transfer_between_rows_possible(bottom_transferred_card, top_row_card):
            # TODO: finish
            pass


    def _take_cards_from_row(self, row_from, card_count):
        cards_to_be_taken = []
        if len(row_from.cards)<card_count:
            self.valid = False
            return None
        if card_count > 1:
            cards_to_be_taken = row_from.cards[-card_count:-1]
            if not cards_to_be_taken[0].face_up:
                self.valid = False
                return None
        else:
            cards_to_be_taken = append(row_from.cards[-1])
        return cards_to_be_taken


    def _transfer_between_rows_possible(self, bottom_transferred_card, top_row_card):
        # TODO: check if ranks of top row card is higher than bottom row
        # TODO: check if colors are not the same
        pass
