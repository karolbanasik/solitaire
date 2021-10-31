class Pile:

    def __init__(self, deck):
        self.cards_face_down = deck.cards
        self.cards_face_up = []
        self.cards = self.cards_face_down + self.cards_face_up

    def flip(self):
        if len(self.cards_face_down) > 0:
            self.cards_face_down[-1].face_up = True
            self.cards_face_up.append(self.cards_face_down[-1])

        elif len(self.cards) == 0:
            print('no cards left on pile')

        else:
            for card in self.cards_face_up:
                card.face_up = False
                self.cards_face_down.append(card)

        self._set_cards()

    def _set_cards(self):
        self.cards = self.cards_face_down + self.cards_face_up
