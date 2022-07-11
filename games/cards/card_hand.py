class CardHand():
    def __init__(self, cards: list):
        self._cards = cards.copy()

    @property
    def cards(self) -> list:
        return self._cards.copy()

    # def play_card(self, index):
    #     if len(self._cards) > 0 and index < len(self._cards) - 1:
    #         card = self._cards[index]
    #         del self._cards[index]
    #         return card
    #     else:
    #         return None

    def add_card(self, card):
        self._cards.append(card)

    def __len__(self):
        return len(self._cards)