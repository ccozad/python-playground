import enum

class PlayingCardSuit(enum.Enum):
    hearts = 1
    diamonds = 2
    clubs = 3
    spades = 4

class PlayingCardValue(enum.Enum):
    ace = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    jack = 11
    queen = 12
    king = 13

class PlayingCard:
    def __init__(self, suit: PlayingCardSuit, value: PlayingCardValue):
        self._suit = suit
        self._value = value
    
    @property
    def suit(self) -> str:
        return self._suit.name
    
    @property
    def value(self) -> str:
        return self._value.name
    
    def __str__(self):
        return '{} of {}'.format(self._value.name, self._suit.name)
    
    def __repr__(self):
        return 'PlayingCard(PlayingCardSuit.{}, PlayingCardValue.{})'.format(self._suit.name, self._value.name)