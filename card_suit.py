class CardSuit:
    name: str = None
    symbol: str = None
    colour: str = None
    suits = {
        'clubs': {'colour': 'black'},
        'hearts': {'colour': 'red'},
        'diamonds': {'colour': 'red'},
        'spades': {'colour': 'black'}
    }

    def __init__(self, name):
        self.name = name
        self.symbol = self.name[0]
        suit_dict = self.suits[self.name]
        self.colour = suit_dict['colour']
