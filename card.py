
class Card:
    suit = None
    rank = None
    face_up = False

    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit
