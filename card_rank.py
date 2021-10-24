
class CardRank:
    rank = None
    ranks = [
        'A',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '10',
        'J',
        'Q',
        'K'
    ]

    def __init__(self, rank_symbol):
        self.rank = rank_symbol