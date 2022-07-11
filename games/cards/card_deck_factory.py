import enum

import games.cards.card_deck as cd
import games.cards.playing_card as pc

class CardDeckType(enum.Enum):
    standard_playing_card = 1

class StandardPlayingCardDeck(cd.CardDeck):
    def __init__(self):
        cards = []
        for suit in pc.PlayingCardSuit:
            for value in pc.PlayingCardValue:
                cards.append(pc.PlayingCard(suit, value))
        self._cards = cards
        self.shuffle()

class CardDeckFactory:
    def get_deck(deck_type):
        if deck_type is CardDeckType.standard_playing_card:
            return StandardPlayingCardDeck()
        else:
            return cd.CardDeck([])



        

