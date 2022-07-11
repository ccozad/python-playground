
import random

class CardDeck():
    def __init__(self, cards: list):
        self._cards = cards.copy()
    
    def shuffle(self):
        random.shuffle(self._cards)

    def draw_card(self):
        if len(self._cards) >= 1:
            return self._cards.pop(0)
        else:
            return None

    def draw_cards(self, count):
        if len(self._cards) >= count and count > 0:
            results = self._cards[:count]
            del self._cards[:count]
            return results
        else:
            return None

    def __len__(self):
        return len(self._cards)